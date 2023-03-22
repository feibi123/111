import pandas as pd
import streamlit as st
from io import StringIO
from streamlit_bokeh_events import streamlit_bokeh_events

# 读取上传的文件
uploaded_file = st.file_uploader("Choose a file")

# 如果用户上传了文件
if uploaded_file is not None:
    # 读取文件内容
    content = uploaded_file.read()

    # 尝试使用 utf-8 编码方式进行解码
    try:
        decoded_content = content.decode('utf-8')
    except UnicodeDecodeError:
        # 如果解码失败，则尝试使用 gbk 编码方式进行解码
        decoded_content = content.decode('gbk')

    # 将解码后的文件内容转换为 pandas 数据框
    df = pd.read_csv(StringIO(decoded_content), skiprows=7)
    
    freeze_table_header = st.bokeh_chart([])

    if df is not None:
        # 使用 st.write 方法展示数据帧
        st.write(df)
        # 使用 streamlit_bokeh_events 库的 with_streamlit 方法，将数据帧和 freeze_table_header 绑定在一起
        with streamlit_bokeh_events(freeze_table_header, events="freeze_table_header"):
            pass
        
