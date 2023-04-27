import streamlit as st
import pandas as pd
import requests
from io import StringIO
from urllib.parse import unquote
st.set_page_config(layout='wide')
# 获取文件夹中所有csv文件的URL列表
url_folder = "https://api.github.com/repos/feibi123/111/contents/广告?ref=main"
response = requests.get(url_folder)
data = response.json()

# 检查 data 变量是否是一个列表
assert isinstance(data, list), f"data is not a list: {data}"

csv_urls = [x["download_url"] for x in data if isinstance(x, dict) and x["name"].endswith(".csv")]

# 读取所有CSV文件并合并为一个DataFrame
dfs = []
for url in csv_urls:
    content = requests.get(url).content.decode("utf-8")
    sheet_name = url.split("/")[-1].split(".")[0]
    df = pd.read_csv(StringIO(content), 
                     usecols=['SKU', '会话次数 – 移动应用', '会话次数 – 移动应用 – B2B', '会话次数 – 浏览器', 
                              '会话次数 – 浏览器 – B2B', '已订购商品数量', '已订购商品数量 - B2B'])
    df["日期"] = pd.to_datetime(unquote(sheet_name), format='%Y年%m月%d日')
    dfs.append(df)
df = pd.concat(dfs, ignore_index=True)
df['手机端访问量'] = df['会话次数 – 移动应用'] + df['会话次数 – 移动应用 – B2B']
df['PC端访问量'] = df['会话次数 – 浏览器'] + df['会话次数 – 浏览器 – B2B']
df['访问量总计'] = df['手机端访问量'] + df['PC端访问量']
df['总订单'] = df['已订购商品数量'] + df['已订购商品数量 - B2B']
df['日期'] = pd.to_datetime(df['日期'])
df['日期'] = df['日期'].dt.date
uploaded_file = st.sidebar.file_uploader("上传产品属性表", type="xlsx")
product_df = pd.read_excel(uploaded_file)
df = pd.merge(df, product_df, on='SKU', how='left')
columns1 = ['日期', '链接名称', '父ASIN', 'SKU', '手机端访问量', 'PC端访问量', '访问量总计', '总订单']
df = df[columns1]

uploaded_file1 = st.sidebar.file_uploader("上传产品属性表", type="xlsx")
dt = pd.read_excel(uploaded_file1)

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



st.table(df)
