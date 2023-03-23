import streamlit as st
import pandas as pd

data = {'姓名': ['小明', '小红', '小刚'],
        '年龄': [18, 19, 20],
        '性别': ['男', '女', '男']}
df = pd.DataFrame(data)

styles = [
    dict(selector='th', props=[('text-align', 'center')]),
    dict(selector='td', props=[('text-align', 'center')])
]

styled_table = df.style.set_table_styles(styles)

st.write(styled_table)
