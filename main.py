import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 冻结表头
css = """
    <style>
        .freeze {
            position: sticky !important;
            top: 0;
            background-color: white;
            z-index: 999;
        }
        .freeze td {
            font-weight: bold;
        }
        .freeze th {
            font-weight: bold;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)
df_html = df.to_html(classes=["freeze"], index=False)

# 显示表格
st.table(df_html, unsafe_allow_html=True)
