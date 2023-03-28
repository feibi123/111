import streamlit as st
import pandas as pd
import numpy as np

# 创建一个包含随机数据的数据框
df = pd.DataFrame(np.random.randn(10, 9), columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'])

# 将数据框转换为 streamlit 表格
table = st.table(df)

# 使用 CSS 样式来设置表格铺满全屏并冻结首行
st.markdown("""
    <style>
        #root > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > div {
            position: fixed !important;
            top: 10% !important;
            left: 5% !important;
            right: 5% !important;
            bottom: 10% !important;
            overflow-y: scroll !important;
            z-index: 0 !important;
        }
        
        #root > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(2) > div > div > div:nth-child(1) > div > div {
            position: sticky !important;
            top: 0 !important;
            z-index: 1 !important;
            background-color: #ffffff !important;
            font-weight: bold !important;
        }
    </style>
""", unsafe_allow_html=True)
