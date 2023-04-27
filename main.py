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
# 在Streamlit中显示数据
st.dataframe(df)
