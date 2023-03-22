import streamlit as st
import pandas as pd
from io import StringIO
uploaded_file1 = st.sidebar.file_uploader("上传订单报告")
 # 将解码后的文件内容转换为 pandas 数据框
df = pd.read_csv(uploaded_file1, skiprows=7)
df = df.dropna(subset=['quantity'])
st.write("""
<style>
    /* 冻结表格首行 */
    .freeze {
        position: sticky;
        top: 0;
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

st.table(df.head(20).style.set_table_attributes("class='freeze'"))
