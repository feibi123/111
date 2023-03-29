import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 将表头固定在页面顶部
st.table(df.style.set_table_styles([{
    'selector': 'thead',
    'props': [('position', 'sticky'), ('top', '0px')]
}]))
