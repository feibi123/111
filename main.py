import codecs
import streamlit as st

# 上传文件
uploaded_file = st.file_uploader("上传文件", type=["csv"])

# 如果上传了文件
if uploaded_file is not None:

    # 检测文件编码
    raw_data = uploaded_file.read()
    try:
        decoded_data = raw_data.decode("utf-8")
    except UnicodeDecodeError:
        decoded_data = raw_data.decode("gbk")

    # 读取文件数据
    with codecs.open(uploaded_file.name, "r", encoding="utf-8") as f:
        data = f.read()

    # 在应用程序中显示数据
    st.write(data)
