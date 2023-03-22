import streamlit as st
import pandas as pd
from io import StringIO
uploaded_file1 = st.sidebar.file_uploader("上传订单报告")
 # 将解码后的文件内容转换为 pandas 数据框
df = pd.read_csv(uploaded_file1, skiprows=7)
df = df.dropna(subset=['quantity'])


# 设置CSS样式
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
    /* 调整表格容器的大小和滚动行为 */
    .table-container {
        height: 500px;
        overflow-y: scroll;
    }
</style>
""", unsafe_allow_html=True)

# 将表格呈现为HTML表格，并对首行应用CSS类
st.write(f'<div class="table-container"><table><thead><tr class="freeze">{"".join([f"<th>{col}</th>" for col in df.columns])}</tr></thead><tbody>{" ".join([f"<tr>{''.join([f'<td>{str(val)}</td>' for val in row.values])}</tr>" for i, row in df.head(20).iterrows()])}</tbody></table></div>', unsafe_allow_html=True)
