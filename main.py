import streamlit as st
import pandas as pd
import io

# 创建文件上传按钮
with st.sidebar:
    uploaded_file = st.file_uploader('上传CSV文件', type=['csv'])

# 如果用户上传了文件，则读取文件
if uploaded_file is not None:
    # 将上传的文件内容转换为字符串，并尝试使用UTF-8-SIG编码和GB2312编码进行读取
    file_content = uploaded_file.read().decode('utf-8-sig')
    if '\uFFFD' in file_content:
        file_content = uploaded_file.read().decode('gb2312')

    # 将字符串转换为pandas的DataFrame，并将第一行作为标题行
    df = pd.read_csv(io.StringIO(file_content), header=0)
    st.write(df)
