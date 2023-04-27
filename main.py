import streamlit as st
import pandas as pd
import requests
from io import StringIO

# 从GitHub下载数据
url = "https://raw.githubusercontent.com/feibi123/111/main/广告/2023年3月10日.csv"
r = requests.get(url)

# 将数据读取为 Pandas 数据框
data = pd.read_csv(StringIO(r.text))

# 在 Streamlit 中显示数据
st.write(data)
