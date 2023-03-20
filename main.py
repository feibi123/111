import streamlit as st

uploaded_file = st.file_uploader("上传文件", type=["csv"], accept_multiple_files=False)

if uploaded_file is not None:
    file_contents = uploaded_file.read()
    st.write("上传的文件内容：")
    st.write(file_contents)
