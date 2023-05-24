from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import streamlit as st
import pandas as pd
import io
# import os
import datetime
import numpy as np
import threading
import plotly.graph_objects as go
st.set_page_config(layout='wide')
pd.set_option('display.max_colwidth', None)
secret_id = 'AKIDaCoNo12sXyMcidM3bv0sdGh6OTbcXWO8'
secret_key = 'jJgrqdGuPmyEXp13tW7Yv9Azf9NSL6e0'
region = 'ap-shanghai'
bucket = 'guang-gao-1318184018'
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key)
client = CosS3Client(config)
folder_key = '广告'

# 获取文件列表
response = client.list_objects(
    Bucket=bucket,
    Prefix=folder_key
)
file_keys = [content['Key'] for content in response['Contents']]


# 线程读取文件的函数
def read_file(file_key):
    # 获取文件内容
    response = client.get_object(
        Bucket=bucket,
        Key=file_key
    )
    content = response['Body'].get_raw_stream().read().decode('utf8')

    # 读取CSV文件数据
    dataframe = pd.read_csv(io.BytesIO(content.encode('utf-8')),
                            usecols=['SKU', '会话次数 – 移动应用', '会话次数 – 移动应用 – B2B', '会话次数 – 浏览器',
                                     '会话次数 – 浏览器 – B2B',
                                     '已订购商品数量', '已订购商品数量 - B2B'])

    # 提取sheet名作为日期列
    sheet_name = file_key.split('/')[-1].split('.')[0]
    dataframe['日期'] = sheet_name

    # 返回读取的数据
    return dataframe


# 多线程读取文件
dataframes = []
lock = threading.Lock()  # 线程锁，用于保护共享资源


def process_data():
    while True:
        with lock:
            if len(file_keys) == 0:
                break
            file_key = file_keys.pop(0)

        dataframe = read_file(file_key)
        with lock:
            dataframes.append(dataframe)


# 创建并启动多个线程
num_threads = min(8, len(file_keys))  # 设置线程数，最多为8个
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=process_data)
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

# 合并所有数据框
df = pd.concat(dataframes, ignore_index=True)
df['手机端访问量'] = df['会话次数 – 移动应用'] + df['会话次数 – 移动应用 – B2B']
df['PC端访问量'] = df['会话次数 – 浏览器'] + df['会话次数 – 浏览器 – B2B']
df['访问量总计'] = df['手机端访问量'] + df['PC端访问量']
df['总订单'] = df['已订购商品数量'] + df['已订购商品数量 - B2B']
df['日期'] = df['日期'].apply(lambda x: datetime.datetime.strptime(x, '%Y年%m月%d日').strftime('%Y-%m-%d'))

file_key1 = '产品属性表.xlsx'
# 获取文件内容
response1 = client.get_object(
    Bucket=bucket,
    Key=file_key1
)
content1 = response1['Body'].get_raw_stream().read()

# 解析 XLSX 文件为数据框
product_df = pd.read_excel(io.BytesIO(content1))
df = pd.merge(df, product_df, on='SKU', how='left')
columns1 = ['日期', '链接名称', '父ASIN', 'SKU', '手机端访问量', 'PC端访问量', '访问量总计', '总订单']
df = df[columns1]

file_key2 = '商品推广 推广的商品 报告.xlsx'
# 获取文件内容
response2 = client.get_object(
    Bucket=bucket,
    Key=file_key2
)
content2 = response2['Body'].get_raw_stream().read()

# 解析 XLSX 文件为数据框
dt = pd.read_excel(io.BytesIO(content2))
dt['日期'] = pd.to_datetime(dt['日期']).dt.strftime('%Y-%m-%d')
dt = dt.rename(columns={'广告SKU': 'SKU'})
dz = dt[dt["广告活动名称"].str.contains("自动")]  # 自动广告汇总
pivot1 = pd.pivot_table(
    dz,
    values=['点击量', '7天总销售量(#)'],
    index=['日期', 'SKU'],
    columns=None,
    aggfunc='sum',
    fill_value=0,
    dropna=True,
    margins=False,
)
pivot1.reset_index(inplace=True)                # 自动广告点击量
pivot1 = pivot1.rename(columns={'点击量': '自动广告点击量'})
pivot1 = pivot1.rename(columns={'7天总销售量(#)': '自动广告销量'})
pivot1 = pd.merge(pivot1, product_df, on='SKU', how='left')
ds = dt[~dt["广告活动名称"].str.contains("自动")]   # 手动广告汇总
pivot2 = pd.pivot_table(
    ds,
    values=['点击量', '7天总销售量(#)'],
    index=['日期', 'SKU'],
    columns=None,
    aggfunc='sum',
    fill_value=0,
    dropna=True,
    margins=False,
)
pivot2.reset_index(inplace=True)                # 自动广告点击量
pivot2 = pivot2.rename(columns={'点击量': '手动广告点击量'})
pivot2 = pivot2.rename(columns={'7天总销售量(#)': '手动广告销量'})
pivot2 = pd.merge(pivot2, product_df, on='SKU', how='left')

pivot = pd.concat([df, pivot1, pivot2], axis=0, ignore_index=True)
pivot = pivot.groupby(['日期', 'SKU', '链接名称', '父ASIN'], as_index=False).sum()
pivot['广告单'] = pivot['手动广告销量'] + pivot['自动广告销量']
pivot['正常单'] = pivot['总订单'] - pivot['广告单']
pivot['正常单'] = np.clip(pivot['正常单'], 0, np.inf)
pivot['正常单占比'] = pivot.apply(lambda x: '{:.2%}'.format(x['正常单'] / x['总订单']) if x['总订单'] != 0 else '0.00%', axis=1)
pivot['综合转化率'] = pivot.apply(
    lambda x: '{:.2%}'.format(x['总订单'] / (x['访问量总计'] + x['自动广告点击量'] + x['手动广告点击量']))
    if x['访问量总计'] + x['自动广告点击量'] + x['手动广告点击量'] != 0 else '0.00%', axis=1)
keep_columns = ['日期', '链接名称', '父ASIN', 'SKU', '手机端访问量', 'PC端访问量', '访问量总计', '自动广告点击量', '手动广告点击量', '广告单', '正常单',
                '总订单', '正常单占比', '综合转化率']
dt = pivot[keep_columns].astype({'手机端访问量': int, 'PC端访问量': int, '访问量总计': int, '自动广告点击量': int, '手动广告点击量': int,
                                 '广告单': int, '正常单': int, '总订单': int})
# print(dt)

# dt.to_csv('E:/广告表/merged_data.csv', index=False, encoding='utf-8-sig')
# df.to_csv('E:/广告表/merged_data.csv', index=False, encoding='utf-8-sig')
#  创建输入框和按钮
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    search_str = st.text_input('请输入查找字符串')
    df_filtered = dt.loc[dt['SKU'].str.contains(search_str, case=False)]

grouped = df_filtered.groupby(['日期']).sum()
da = pd.DataFrame({'日期': grouped.index, '手机端访问量': grouped['手机端访问量'], 'PC端访问量': grouped['PC端访问量'],
                   '访问量总计': grouped['访问量总计'], '自动广告点击量': grouped['自动广告点击量'], '手动广告点击量': grouped['手动广告点击量'],
                   '广告单': grouped['广告单'], '正常单': grouped['正常单'], '总订单': grouped['总订单']})
da['正常单占比'] = da.apply(lambda x: '{:.2%}'.format(x['正常单'] / x['总订单']) if x['总订单'] != 0 else '0.00%', axis=1)
da['综合转化率'] = da.apply(
    lambda x: '{:.2%}'.format(x['总订单'] / (x['访问量总计'] + x['自动广告点击量'] + x['手动广告点击量']))
    if x['访问量总计'] + x['自动广告点击量'] + x['手动广告点击量'] != 0 else '0.00%', axis=1)

with row1_col2:
    start_date = st.date_input('选择开始日期', value=pd.to_datetime(da['日期'].min()),
                               min_value=pd.to_datetime(da['日期'].min()), max_value=pd.to_datetime(da['日期'].max()))
with row1_col3:
    end_date = st.date_input('选择结束日期', value=pd.to_datetime(da['日期'].max()),
                             min_value=pd.to_datetime(da['日期'].min()), max_value=pd.to_datetime(da['日期'].max()))

# 根据选择的日期过滤数据
dx = da[(da['日期'] >= start_date.strftime('%Y-%m-%d')) & (da['日期'] <= end_date.strftime('%Y-%m-%d'))]


fig_data = list()
fig_data.append(go.Bar(x=pd.to_datetime(dx['日期']), y=dx['手机端访问量'], name='手机端访问量',
                       marker=dict(color='rgb(192, 207, 58)')))
fig_data.append(go.Bar(x=pd.to_datetime(dx['日期']), y=dx['PC端访问量'], name='PC端访问量',
                       marker=dict(color='rgb(216, 196, 143)')))
fig_data.append(go.Bar(x=pd.to_datetime(dx['日期']), y=dx['访问量总计'], name='访问量总计',
                       marker=dict(color='rgb(84, 158, 57)')))
fig_data.append(go.Bar(x=pd.to_datetime(dx['日期']), y=dx['自动广告点击量'], name='自动广告点击量',
                       marker=dict(color='rgb(254, 236, 136)')))
fig_data.append(go.Bar(x=pd.to_datetime(dx['日期']), y=dx['手动广告点击量'], name='手动广告点击量',
                       marker=dict(color='rgb(2, 150, 118)')))
fig_data.append(go.Scatter(x=pd.to_datetime(dx['日期']), y=dx['广告单'], mode='lines+markers', name='广告单',
                           marker=dict(color='rgb(216, 196, 143)')))
fig_data.append(go.Scatter(x=pd.to_datetime(dx['日期']), y=dx['正常单'], mode='lines+markers', name='正常单',
                           marker=dict(color='rgb(173, 224, 95)')))
fig_data.append(go.Scatter(x=pd.to_datetime(dx['日期']), y=dx['总订单'], mode='lines+markers', name='总订单',
                           marker=dict(color='rgb(2, 150, 118)')))
fig_data.append(go.Scatter(x=pd.to_datetime(dx['日期']), y=dx['正常单占比'], mode='lines+markers', name='正常单占比', yaxis='y2',
                           marker=dict(color='#000000')))
fig_data.append(go.Scatter(x=pd.to_datetime(dx['日期']), y=dx['综合转化率'], mode='lines+markers', name='综合转化率', yaxis='y2',
                           marker=dict(color='#FF0000')))
# 将两个图表合并成一个
combined_fig = go.Figure(data=fig_data,
                         layout=go.Layout(title=dict(text='SKU广告趋势图', x=0.5, y=0.9),
                                          xaxis=dict(tickformat='%Y-%m-%d', dtick='D'),
                                          yaxis2=dict(side='right', overlaying='y', showgrid=False, tickfont={})))

st.plotly_chart(combined_fig, use_container_width=True)
st.write(dt)
