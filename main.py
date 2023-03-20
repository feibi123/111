import streamlit as st
import pandas as pd
import io
import chardet

# 创建文件上传按钮
with st.sidebar:
    uploaded_file = st.file_uploader('上传CSV文件', type=['csv'])

# 如果用户上传了文件，则读取文件
if uploaded_file is not None:
    # 使用chardet库自动检测文件编码
    file_content = uploaded_file.read()
    file_encoding = chardet.detect(file_content)['encoding']

    # 根据文件编码读取文件内容
    file_content = file_content.decode(file_encoding)

    # 将文件内容转换为pandas的DataFrame，并将第一行作为标题行
    df = pd.read_csv(io.StringIO(file_content), header=0)
    st.write(df)
