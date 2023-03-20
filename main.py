import streamlit as st

uploaded_file = st.file_uploader("选择文件", type=None)

if uploaded_file is not None:
    # 处理上传的文件
    contents = uploaded_file.read()
    st.write("上传的文件内容为：", contents)
