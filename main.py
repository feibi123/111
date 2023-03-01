import streamlit as st
import pandas as pd
uploaded_file1 = st.file_uploader("上传在途库存", type="csv")  # 读取在途库存，并将首行作为标题列
dt = pd.read_csv(uploaded_file1, header=0)
st.dataframe(df)
