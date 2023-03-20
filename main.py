import streamlit as st
import pandas as pd
uploaded_file1 = st.sidebar.file_uploader("上传订单报告", type="csv")
if uploaded_file1 is not None:
    df = pd.read_csv(uploaded_file1, header=None)
    st.table(df)
else:
    st.write("请上传CSV文件")
