import streamlit as st
import pandas as pd
import io
import codecs

# 创建文件上传按钮
with st.sidebar:
    uploaded_file = st.file_uploader('上传CSV文件', type=['csv'])

# 如果用户上传了文件，则读取文件
if uploaded_file is not None:
    # 读取文件内容并设定文件编码为 GB2312
    file_content = uploaded_file.read().decode('GB2312', 'ignore')

    # 将文件内容转换为pandas的DataFrame，并将第一行作为标题行
    df = pd.read_csv(io.StringIO(file_content), header=0)
    st.write(df)
