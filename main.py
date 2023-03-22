import pandas as pd
import streamlit as st
from io import StringIO

# 读取上传的文件
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
    
     
if 'df' in locals():
    st.markdown("<style>.css-q4dj2t th, .css-1a6erhd {position: sticky; top: 0;}</style>", unsafe_allow_html=True)
    st.table(df)
    
    
