import streamlit as st
import pandas as pd

pd.set_option('display.max_colwidth', None)
st.set_page_config(layout="wide")

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 显示表格
st.write(df)
