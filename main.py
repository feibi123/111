import streamlit as st
import pandas as pd
import codecs
from io import StringIO

# 创建上传文件的按钮
uploaded_file = st.file_uploader("Upload a file", type=["csv"])

# 读取文件内容并转换成DataFrame格式
if uploaded_file is not None:
    # 通过codecs模块自动检测文件编码
    raw_text = codecs.decode(uploaded_file.read(), codecs.BOM_UTF8, 'utf-8')
    df = pd.read_csv(StringIO(raw_text))
    st.write(df)
    
