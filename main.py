import streamlit as st
import pandas as pd
import requests
from io import StringIO

# 获取文件夹中所有csv文件的URL列表
url_folder = "https://api.github.com/repos/feibi123/111/contents/广告?ref=main"
response = requests.get(url_folder)
data = response.json()
csv_urls = [x["download_url"] for x in data if x["name"].endswith(".csv")]

# 读取所有CSV文件并合并为一个DataFrame
df = pd.concat([pd.read_csv(StringIO(requests.get(url).text)) for url in csv_urls])

# 在Streamlit中显示数据
st.dataframe(df)
