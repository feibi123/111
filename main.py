import streamlit as st
import pandas as pd
import codecs

# 设置页面标题
st.title("上传 CSV 文件示例")

# 创建上传按钮
uploaded_file = st.file_uploader("上传 CSV 文件", type="csv")

# 如果用户上传了文件
if uploaded_file is not None:
    # 读取文件内容并解码
    content = uploaded_file.read()
    decoded_content = codecs.decode(content, 'utf-8-sig') # 解码为 utf-8

    # 尝试使用 Pandas 读取 utf-8 编码的文件
    try:
        df = pd.read_csv(StringIO(decoded_content), skiprows=7)
    except:
        # 如果读取失败，尝试使用 Pandas 读取 gbk 编码的文件
        df = pd.read_csv(StringIO(decoded_content), skiprows=7, encoding='gbk')

    # 显示数据框
    st.write(df)
