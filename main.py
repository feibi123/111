import io
import pandas as pd
import streamlit as st

uploaded_file1 = st.sidebar.file_uploader("上传订单报告", type="csv")

if uploaded_file1 is not None:
    # 将文件内容读取到内存中
    file_contents = uploaded_file1.read()
    
    # 将字节数据转换为文本数据
    file_text = io.TextIOWrapper(io.BytesIO(file_contents), encoding='gbk').read()
    
    # 使用pandas读取csv文件
    df = pd.read_csv(io.StringIO(file_text), header=None)
    
    # 显示数据
    st.write(df)
