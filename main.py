import subprocess

subprocess.check_call(["pip", "install", "chardet"])

import streamlit as st
import chardet

# 上传文件并读取文件内容
uploaded_file = st.file_uploader("上传文件", type=["csv"])
if uploaded_file is not None:
    # 读取文件内容
    content = uploaded_file.getvalue()
    
    # 自动检测文件编码
    result = chardet.detect(content)
    file_encoding = result["encoding"]
    
    # 使用检测到的编码读取文件
    if file_encoding is not None:
        st.write(f"文件编码: {file_encoding}")
        content = content.decode(file_encoding)
    else:
        st.write("未能检测到文件编码")
    
    # 将文件内容转换为 Pandas DataFrame
    df = pd.read_csv(io.StringIO(content), header=0)
    st.write(df)
