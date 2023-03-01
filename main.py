import streamlit as st
import pandas as pd
uploaded_file2 = st.file_uploader("上传即时库存", type="csv")
dk = pd.read_csv(uploaded_file2, header=0, encoding='gbk') 
st.dataframe(df)
