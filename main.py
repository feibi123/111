import streamlit as st
import pandas as pd
from io import StringIO

pd.set_option('display.max_colwidth', None)
st.set_page_config(layout="wide")
df = pd.DataFrame()
# 添加上传文件的按钮
uploaded_file = st.file_uploader("Choose a file")

# 如果用户上传了文件
if uploaded_file is not None:
    # 读取文件内容
    content = uploaded_file.read()

    # 尝试使用 utf-8 编码方式进行解码
    try:
        decoded_content = content.decode('utf-8')
    except UnicodeDecodeError:
        # 如果解码失败，则尝试使用 gbk 编码方式进行解码
        decoded_content = content.decode('gbk')

    # 将解码后的文件内容转换为 pandas 数据框
    df = pd.read_csv(StringIO(decoded_content), skiprows=7)

    
df = df.dropna(subset=['quantity'])  # 删除含有空值的行
df['quantity'] = df['quantity'].astype(int)  # 将quantity列转换成整数类型
df = df.dropna(subset=['type'])   # 删除含有空值的行
df = df[df['type'].str.contains('Order')]  # 从type列筛选出Order
df = df[['date/time', 'sku', 'quantity']]


if not df.empty:
    st.write(
        f"""
        <style>
            .stTable thead th {{
                position: sticky;
                top: 0;
                background-color: white;
                z-index: 999;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    
st.table(df)
