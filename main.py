import streamlit as st
import pandas as pd
uploaded_file3 = st.file_uploader("上传产品属性表", type="xlsx")  # 读取产品属性表，并将首行作为标题列
dc = pd.read_excel(uploaded_file3, header=0)
st.dataframe(df)
