import os
import pandas as pd
import datetime
import numpy as np
import streamlit as st
import plotly.graph_objects as go
st.set_page_config(layout='wide')
# 获取目录下所有CSV文件的文件名
directory = st.text_input("请输入文件夹路径：")
csv_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.csv')]

# 读取所有CSV文件并合并到一个数据框中
df_list = []
for file in csv_files:
    sheet_name = os.path.splitext(os.path.basename(file))[0]  # 获取文件名作为sheet名
    df = pd.read_csv(file, encoding='utf-8-sig',
                     usecols=['SKU', '会话次数 – 移动应用', '会话次数 – 移动应用 – B2B', '会话次数 – 浏览器', '会话次数 – 浏览器 – B2B',
                              '已订购商品数量', '已订购商品数量 - B2B'])
    df['日期'] = sheet_name  # 添加日期列
    df_list.append(df)
df = pd.concat(df_list, axis=0)
df['手机端访问量'] = df['会话次数 – 移动应用'] + df['会话次数 – 移动应用 – B2B']
df['PC端访问量'] = df['会话次数 – 浏览器'] + df['会话次数 – 浏览器 – B2B']
df['访问量总计'] = df['手机端访问量'] + df['PC端访问量']
df['总订单'] = df['已订购商品数量'] + df['已订购商品数量 - B2B']
df['日期'] = df['日期'].apply(lambda x: datetime.datetime.strptime(x, '%Y年%m月%d日').strftime('%Y-%m-%d'))

product_file = 'E:/广告表/产品属性表.xlsx'
product_df = pd.read_excel(product_file)
df = pd.merge(df, product_df, on='SKU', how='left')
columns1 = ['日期', '链接名称', '父ASIN', 'SKU', '手机端访问量', 'PC端访问量', '访问量总计', '总订单']
df = df[columns1]

dt = 'E:/广告表/商品推广 推广的商品 报告.xlsx'
dt = pd.read_excel(dt)
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

sku_list = sorted(dt['SKU'].unique())

# 在页面上方添加选择 SKU 的下拉菜单
selected_sku = st.selectbox('选择 SKU', sku_list)

# 过滤数据框以仅显示所选 SKU 的数据
df = dt[dt['SKU'] == selected_sku]
df = df.drop_duplicates(subset=['SKU', '日期'])
start_date = st.date_input('选择开始日期', value=pd.to_datetime(df['日期'].min()), min_value=pd.to_datetime(df['日期'].min()),
                           max_value=pd.to_datetime(df['日期'].max()))
end_date = st.date_input('选择结束日期', value=pd.to_datetime(df['日期'].max()), min_value=pd.to_datetime(df['日期'].min()),
                         max_value=pd.to_datetime(df['日期'].max()))

# 根据选择的日期过滤数据
df = df[(df['日期'] >= start_date.strftime('%Y-%m-%d')) & (df['日期'] <= end_date.strftime('%Y-%m-%d'))]

fig_data = list()
fig_data.append(go.Bar(x=pd.to_datetime(df['日期']), y=df['手机端访问量'], name='手机端访问量'))
fig_data.append(go.Bar(x=pd.to_datetime(df['日期']), y=df['PC端访问量'], name='PC端访问量'))
fig_data.append(go.Bar(x=pd.to_datetime(df['日期']), y=df['访问量总计'], name='访问量总计'))
fig_data.append(go.Bar(x=pd.to_datetime(df['日期']), y=df['自动广告点击量'], name='自动广告点击量'))
fig_data.append(go.Bar(x=pd.to_datetime(df['日期']), y=df['手动广告点击量'], name='手动广告点击量'))
fig_data.append(go.Scatter(x=pd.to_datetime(df['日期']), y=df['广告单'], mode='lines+markers', name='广告单'))
fig_data.append(go.Scatter(x=pd.to_datetime(df['日期']), y=df['正常单'], mode='lines+markers', name='正常单'))
fig_data.append(go.Scatter(x=pd.to_datetime(df['日期']), y=df['总订单'], mode='lines+markers', name='总订单'))
fig_data.append(go.Scatter(x=pd.to_datetime(df['日期']), y=df['正常单占比'], mode='lines+markers', name='正常单占比'))
fig_data.append(go.Scatter(x=pd.to_datetime(df['日期']), y=df['综合转化率'], mode='lines+markers', name='综合转化率'))
# 将两个图表合并成一个
combined_fig = go.Figure(data=fig_data,
                         layout=go.Layout(title=dict(text='SKU广告趋势图', x=0.5, y=0.9),
                                          xaxis=dict(tickformat='%Y-%m-%d', dtick='D')))

st.plotly_chart(combined_fig, use_container_width=True)
st.table(dt)
