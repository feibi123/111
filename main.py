import pandas as pd
import streamlit as st

uploaded_file = st.sidebar.file_uploader("上传订单报告", type="csv")

if uploaded_file is not None:
    # 使用 Pandas 读取 CSV 文件
    df = pd.read_csv(uploaded_file, header=None, sep = '\t')
    # 显示数据框
    st.write(df)
