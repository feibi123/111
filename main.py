import streamlit as st
import pandas as pd
uploaded_file = st.file_uploader("上传订单报告", type="csv")
df = pd.read_csv(uploaded_file, header=None, encoding='gbk')  # header=None 参数禁止将第一行读入为列标题
df = df.drop(df.index[:7]) 
st.dataframe(df)
