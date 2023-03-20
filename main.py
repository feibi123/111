import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose an XLSX file", type="xlsx")

if uploaded_file is not None:
    # 使用 Pandas 库中的 read_excel 函数读取 XLSX 文件
    df = pd.read_excel(uploaded_file)
    st.write("File content:")
    st.write(df)
