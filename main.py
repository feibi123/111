import streamlit as st
import pandas as pd
uploaded_file = st.sidebar.file_uploader("上传产品属性表", type="csv")
df = pd.read_csv(uploaded_file)
st.table(df)
