import streamlit as st
import pandas as pd
uploaded_file1 = st.sidebar.file_uploader("上传订单报告", type="csv")
df = pd.read_csv(uploaded_file1, header=None, encoding='GB2312')
st.table(df)

