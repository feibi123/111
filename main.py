import streamlit as st
import pandas as pd

# 从GitHub加载数据
url = "https://raw.githubusercontent.com/feibi123/111.git/main/广告/2023年3月10日.csv"
data = pd.read_csv(url)

# 在Streamlit中显示数据
st.dataframe(data)
