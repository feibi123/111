import pandas as pd
import streamlit as st

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 在Streamlit中显示表格，并将表格全屏并冻结首行
st.write(df.style.set_table_styles(
    [{"selector": "thead", "props": [("position", "sticky"), ("top", "0px")]}]
).set_properties(**{'width': '100%', 'height': '100vh', 'max-height': 'none', 'overflow-y': 'auto'}))
