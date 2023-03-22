import pandas as pd
import streamlit as st
from io import StringIO

pd.set_option('display.max_colwidth', None)
st.set_page_config(layout="wide")
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
    
     
if 'df' in locals():
    # 添加 css 样式
    st.markdown("""
        <style>
            .dataframe th {
                position: sticky;
                top: 0;
                background-color: #FFFFFF;
                z-index: 1;
            }
            .dataframe tbody tr:first-child th {
                position: sticky;
                left: 0;
                z-index: 0;
            }
        </style>
    """, unsafe_allow_html=True)
    

    styles = [
        {'selector': 'th', 'props': [('font-size', '16px'), ('text-align', 'center')]},
        {'selector': 'td', 'props': [('font-size', '14px'), ('text-align', 'center')]},
        {'selector': 'tr:hover td', 'props': [('background-color', '#f5f5f5')]}
    ]
    st.write(df.style.set_table_styles(styles), unsafe_allow_html=True)
