import streamlit as st
import pandas as pd
uploaded_file1 = st.sidebar.file_uploader("上传订单报告", type="csv")
df = pd.read_csv(uploaded_file1, header=None)  # header=None 参数禁止将第一行读入为列标题
df = df.drop(df.index[:7])  # 删除前7行
st.table(df)
