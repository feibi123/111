import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 使用 CSS 控制表格样式
st.write("""
    <style>
        div[data-testid="stTable"] thead {
            position: sticky;
            top: 0;
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

# 显示表格
st.table(df)
