import streamlit as st
import pandas as pd
uploaded_file = st.sidebar.file_uploader("上传产品属性表", type="xlsx")
df = pd.read_excel(uploaded_file, header=0,
st.table(df)
