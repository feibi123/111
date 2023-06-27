from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import streamlit as st
import pandas as pd
import io
import os
import datetime
import numpy as np
import plotly.graph_objects as go
pd.set_option('display.max_colwidth', None)
st.set_page_config(layout='wide')
secret_id = 'AKIDU1LGySgfRzrY5TfcvsdARSHuHSs8ByWr'
secret_key = 'B6wRmtlOrAPRDnAJCvRilLk5LtJYZLel'
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

# 读取并合并文件数据
dataframes = []
for file_key in file_keys:
    # 获取文件内容
    response = client.get_object(
        Bucket=bucket,
        Key=file_key
    )
    content = response['Body'].get_raw_stream().read().decode('utf8')

    # 读取CSV文件数据
    dataframe = pd.read_csv(io.BytesIO(content.encode('utf-8')),
                            usecols=['SKU', '会话次数 – 移动应用', '会话次数 – 移动应用 – B2B', '会话次数 – 浏览器', '会话次数 – 浏览器 – B2B',
                                     '已订购商品数量', '已订购商品数量 - B2B', '已订购商品销售额', '已订购商品销售额 - B2B'])

    # 提取sheet名作为日期列
    sheet_name = os.path.basename(file_key).split('.')[0]
    dataframe['日期'] = sheet_name

    # 将数据框添加到列表
    dataframes.append(dataframe)


df = pd.concat(dataframes, ignore_index=True)
df['手机端访问量'] = df['会话次数 – 移动应用'] + df['会话次数 – 移动应用 – B2B']
df['PC端访问量'] = df['会话次数 – 浏览器'] + df['会话次数 – 浏览器 – B2B']
df['访问量总计'] = df['手机端访问量'] + df['PC端访问量']
df['总订单'] = df['已订购商品数量'] + df['已订购商品数量 - B2B']
df['已订购商品销售额'] = df['已订购商品销售额'].str.replace(r'[^\d.]', '', regex=True).astype(float)
df['已订购商品销售额 - B2B'] = df['已订购商品销售额 - B2B'].str.replace(r'[^\d.]', '', regex=True).astype(float)
df['总销售额'] = df['已订购商品销售额'] + df['已订购商品销售额 - B2B']
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
dfa = df[columns1]
columns2 = ['日期', '链接名称', '父ASIN', 'SKU', '访问量总计', '总订单', '总销售额']
dfb = df[columns2]

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
dt = pd.merge(dt, product_df, on='SKU', how='left')
dt = dt.rename(columns={'7天总销售额': '广告销售额'})
dt = dt.rename(columns={'7天总销售量(#)': '广告销量'})
columns3 = ['日期', '链接名称', '父ASIN', 'SKU', '点击量', '花费', '广告销售额', '广告销量']
dta = dt[columns3]

pivota = pd.concat([dfb, dta], axis=0, ignore_index=True)
pivota = pivota.groupby(['日期', '链接名称', '父ASIN'], as_index=False).sum()
pivota['日期'] = pd.to_datetime(pivota['日期'])
df1 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=6))]  # 截取近7天的数据
df1 = df1.groupby(['父ASIN'])['总订单'].sum().reset_index()
df1 = df1.rename(columns={'总订单': '7天总订单'})
df2 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=14))]  # 截取近15天的数据
df2 = df2.groupby(['父ASIN'])['总订单'].sum().reset_index()
df2 = df2.rename(columns={'总订单': '15天总订单'})
df3 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=29))]  # 截取近30天的数据
df3 = df3.groupby(['父ASIN'])['总订单'].sum().reset_index()
df3 = df3.rename(columns={'总订单': '30天总订单'})
df4 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=29))]  # 截取近30天的数据
df4 = df4.groupby(['父ASIN'])['广告销量'].sum().reset_index()
df4 = df4.rename(columns={'广告销量': '30天广告销量'})
df5 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=29))]  # 截取近30天的数据
df5 = df5.groupby(['父ASIN'])['花费'].sum().reset_index()
df5 = df5.rename(columns={'花费': '30天广告花费'})
df6 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=29))]  # 截取近30天的数据
df6 = df6.groupby(['父ASIN'])['广告销售额'].sum().reset_index()
df6 = df6.rename(columns={'广告销售额': '30天广告销售额'})
df7 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=29))]  # 截取近30天的数据
df7 = df7.groupby(['父ASIN'])['总销售额'].sum().reset_index()
df7 = df7.rename(columns={'总销售额': '30天总销售额'})
df8 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=29))]  # 截取近30天的数据
df8 = df8.groupby(['父ASIN'])['访问量总计'].sum().reset_index()
df8 = df8.rename(columns={'访问量总计': '30天访问量'})
df9 = pivota[pivota['日期'] >= (pivota['日期'].max() - pd.Timedelta(days=29))]  # 截取近30天的数据
df9 = df9.groupby(['父ASIN'])['点击量'].sum().reset_index()
df9 = df9.rename(columns={'点击量': '30天点击量'})

tables = [df1, df2, df3, df4, df5, df6, df7, df8, df9]
# 初始化合并结果为第一个小表格
merged_df = tables[0]

# 循环合并剩余的小表格
for i in range(1, len(tables)):
    merged_df = pd.merge(merged_df, tables[i], on='父ASIN', how='outer')

merged_df.fillna(0, inplace=True)
merged_df['广告Acos'] = merged_df.apply(
    lambda x: '{:.2%}'.format(x['30天广告花费'] / x['30天广告销售额']) if x['30天广告销售额'] != 0 else '0.00%', axis=1)
merged_df['广告花费占比'] = merged_df.apply(
    lambda x: '{:.2%}'.format(x['30天广告花费'] / x['30天总销售额']) if x['30天总销售额'] != 0 else '0.00%', axis=1)
merged_df['转化率'] = merged_df.apply(
    lambda x: '{:.2%}'.format(x['30天总订单'] / (x['30天访问量'] + x['30天点击量']))
    if x['30天访问量'] + x['30天点击量'] != 0 else '0.00%', axis=1)

merged_df[['7天总订单', '15天总订单', '30天总订单', '30天广告销量', '30天访问量', '30天点击量']] = \
    merged_df[['7天总订单', '15天总订单', '30天总订单', '30天广告销量', '30天访问量', '30天点击量']].round().astype(int)  # 保留整数
merged_df[['30天广告花费', '30天广告销售额', '30天总销售额']] = \
    merged_df[['30天广告花费', '30天广告销售额', '30天总销售额']].applymap(lambda x: '{:.2f}'.format(x))

dz = dt[dt["广告活动名称"].str.contains("自动")]  # 自动广告汇总

pivot1 = pd.pivot_table(
    dz,
    values=['点击量', '广告销量'],
    index=['日期', 'SKU'],
    columns=None,
    aggfunc='sum',
    fill_value=0,
    dropna=True,
    margins=False,
)
pivot1.reset_index(inplace=True)                # 自动广告点击量
pivot1 = pivot1.rename(columns={'点击量': '自动广告点击量'})
pivot1 = pivot1.rename(columns={'广告销量': '自动广告销量'})
pivot1 = pd.merge(pivot1, product_df, on='SKU', how='left')
ds = dt[~dt["广告活动名称"].str.contains("自动")]   # 手动广告汇总
pivot2 = pd.pivot_table(
    ds,
    values=['点击量', '广告销量'],
    index=['日期', 'SKU'],
    columns=None,
    aggfunc='sum',
    fill_value=0,
    dropna=True,
    margins=False,
)
pivot2.reset_index(inplace=True)                # 自动广告点击量
pivot2 = pivot2.rename(columns={'点击量': '手动广告点击量'})
pivot2 = pivot2.rename(columns={'广告销量': '手动广告销量'})
pivot2 = pd.merge(pivot2, product_df, on='SKU', how='left')

pivot = pd.concat([dfa, pivot1, pivot2], axis=0, ignore_index=True)
pivot = pivot.groupby(['日期', 'SKU', '链接名称', '父ASIN'], as_index=False).sum()
pivot['广告单'] = pivot['手动广告销量'] + pivot['自动广告销量']
pivot['自然单'] = pivot['总订单'] - pivot['广告单']
pivot['自然单'] = np.clip(pivot['自然单'], 0, np.inf)

keep_columns = ['日期', '链接名称', '父ASIN', 'SKU', '手机端访问量', 'PC端访问量', '访问量总计', '自动广告点击量', '手动广告点击量', '广告单', '自然单',
                '总订单']
dt = pivot[keep_columns].astype({'手机端访问量': int, 'PC端访问量': int, '访问量总计': int, '自动广告点击量': int, '手动广告点击量': int,
                                 '广告单': int, '自然单': int, '总订单': int})

button_style = "<style>div.stButton > button{width: 200px; height: 50px; font-size: 18px;}</style>"
st.markdown(button_style, unsafe_allow_html=True)
button_home = st.sidebar.button("广告总表")
button_settings = st.sidebar.button("广告分表")
if button_home:
    # 显示广告总表
    row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)
    with row1_col1:
        parent_asin_input = st.empty()
    with row1_col2:
        sku_input = st.empty()
    with row1_col3:
        start_date_input = st.empty()
    with row1_col4:
        end_date_input = st.empty()

    st.table(merged_df)
else:
    # 根据模糊查找条件过滤数据
    filtered_data = dt.copy()
    row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)
    with row1_col1:
        parent_asin_input = st.text_input("输入父ASIN")
    with row1_col2:
        sku_input = st.text_input("输入SKU")
    with row1_col3:
        start_date_input = st.date_input("选择开始日期")
    with row1_col4:
        end_date_input = st.date_input("选择结束日期")

    if parent_asin_input:
        filtered_data = filtered_data[filtered_data['父ASIN'].str.contains(parent_asin_input, case=False)]

    if start_date_input and end_date_input:
        start_date_str = start_date_input.strftime("%Y-%m-%d")
        end_date_str = end_date_input.strftime("%Y-%m-%d")
        filtered_data = filtered_data[(filtered_data['日期'] >= start_date_str) & (filtered_data['日期'] <= end_date_str)]

    if parent_asin_input and not sku_input:
        summary_data = filtered_data.groupby(['日期', '父ASIN']).agg({
            '链接名称': 'first',
            '手机端访问量': 'sum',
            'PC端访问量': 'sum',
            '访问量总计': 'sum',
            '自动广告点击量': 'sum',
            '手动广告点击量': 'sum',
            '广告单': 'sum',
            '自然单': 'sum',
            '总订单': 'sum'
        }).reset_index()
    else:
        sku_related_data = filtered_data[filtered_data['SKU'].str.contains(sku_input, case=False)]
        sku_first = sku_input if not sku_related_data.empty else ''
        summary_data = sku_related_data.groupby(['日期', '父ASIN']).agg({
            '链接名称': 'first',
            'SKU': lambda x: sku_first,
            '手机端访问量': 'sum',
            'PC端访问量': 'sum',
            '访问量总计': 'sum',
            '自动广告点击量': 'sum',
            '手动广告点击量': 'sum',
            '广告单': 'sum',
            '自然单': 'sum',
            '总订单': 'sum'
        }).reset_index()

    # 添加正常单占比列
    summary_data['自然单占比'] = summary_data.apply(
        lambda x: '{:.2%}'.format(x['自然单'] / x['总订单']) if x['总订单'] != 0 else '0.00%', axis=1)

    summary_data['综合转化率'] = summary_data.apply(
        lambda x: '{:.2%}'.format(x['总订单'] / (x['访问量总计'] + x['自动广告点击量'] + x['手动广告点击量']))
        if x['访问量总计'] + x['自动广告点击量'] + x['手动广告点击量'] != 0 else '0.00%', axis=1)

    fig_data = list()
    fig_data.append(go.Bar(x=summary_data['日期'], y=summary_data['手机端访问量'], name='手机端访问量',
                           marker=dict(color='rgb(192, 207, 58)')))
    fig_data.append(go.Bar(x=summary_data['日期'], y=summary_data['PC端访问量'], name='PC端访问量',
                           marker=dict(color='rgb(216, 196, 143)')))
    fig_data.append(go.Bar(x=summary_data['日期'], y=summary_data['访问量总计'], name='访问量总计',
                           marker=dict(color='rgb(84, 158, 57)')))
    fig_data.append(go.Bar(x=summary_data['日期'], y=summary_data['自动广告点击量'], name='自动广告点击量',
                           marker=dict(color='rgb(254, 236, 136)')))
    fig_data.append(go.Bar(x=summary_data['日期'], y=summary_data['手动广告点击量'], name='手动广告点击量',
                           marker=dict(color='rgb(2, 150, 118)')))
    fig_data.append(go.Scatter(x=summary_data['日期'], y=summary_data['广告单'], mode='lines+markers', name='广告单',
                               marker=dict(color='rgb(216, 196, 143)')))
    fig_data.append(go.Scatter(x=summary_data['日期'], y=summary_data['自然单'], mode='lines+markers', name='自然单',
                               marker=dict(color='rgb(173, 224, 95)')))
    fig_data.append(go.Scatter(x=summary_data['日期'], y=summary_data['总订单'], mode='lines+markers', name='总订单',
                               marker=dict(color='rgb(2, 150, 118)')))
    fig_data.append(
        go.Scatter(x=summary_data['日期'], y=summary_data['自然单占比'], mode='lines+markers', name='自然单占比',
                   yaxis='y2', marker=dict(color='#000000')))
    fig_data.append(
        go.Scatter(x=summary_data['日期'], y=summary_data['综合转化率'], mode='lines+markers', name='综合转化率',
                   yaxis='y2', marker=dict(color='#FF0000')))
    # 将两个图表合并成一个
    combined_fig = go.Figure(data=fig_data,
                             layout=go.Layout(title=dict(text='SKU广告趋势图', x=0.5, y=0.9),
                                              xaxis=dict(tickformat='%Y-%m-%d', dtick='D'),
                                              yaxis2=dict(side='right', overlaying='y', showgrid=False, tickfont={})))

    with st.expander("展开分表", expanded=True):
        st.markdown('<style>div.css-1l02zno table {width: 100%;}</style>', unsafe_allow_html=True)
        st.table(summary_data)
    st.plotly_chart(combined_fig, use_container_width=True)
