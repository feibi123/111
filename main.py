import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 添加CSS样式
st.markdown("""
            <style>
            table td:nth-child(1) {
                position: -webkit-sticky;
                position: sticky;
                left: 0;
                background-color: white;
                z-index: 1;
            }
            </style>
            """, unsafe_allow_html=True)

# 显示表格
st.table(df)
