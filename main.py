# import streamlit as st
# import pandas as pd
# import requests
# from io import StringIO

# # 获取文件夹中所有csv文件的URL列表
# url_folder = "https://api.github.com/repos/feibi123/111/contents/广告?ref=main"
# response = requests.get(url_folder)
# data = response.json()
# csv_urls = [x["download_url"] for x in data if x["name"].endswith(".csv")]

# # 读取所有CSV文件并合并为一个DataFrame
# df = pd.concat([pd.read_csv(StringIO(requests.get(url).text)) for url in csv_urls])

# # 在Streamlit中显示数据
# st.dataframe(df)
import streamlit as st
import pandas as pd
import requests
from io import StringIO
from urllib.parse import unquote

# 获取文件夹中所有csv文件的URL列表
url_folder = "https://api.github.com/repos/feibi123/111/contents/广告?ref=main"
response = requests.get(url_folder)
data = response.json()
csv_urls = [x["download_url"] for x in data if x["name"].endswith(".csv")]

# 读取所有CSV文件并合并为一个DataFrame
dfs = []
for url in csv_urls:
    content = requests.get(url).content.decode("utf-8")
    sheet_name = url.split("/")[-1].split(".")[0]
    df = pd.read_csv(StringIO(content))
    df["sheet_name"] = pd.to_datetime(unquote(sheet_name), format='%Y年%m月%d日')
    dfs.append(df)
df = pd.concat(dfs)

# 在Streamlit中显示数据
st.dataframe(df)
