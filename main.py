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
        z-index: 1;
        background-color: white;
        font-weight: bold;
    }
    /* 设置表格边框和宽度 */
    table {
        border-collapse: collapse;
        width: 100%;
    }
    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# 将表格呈现为HTML表格，并对首行应用CSS类
st.write(df.head(20).to_html(index=False, classes=["freeze", "table"], escape=False), unsafe_allow_html=True)
