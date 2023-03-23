import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 设置首行冻结样式
styles = [dict(selector="th", props=[("position", "sticky"), ("top", "0"), ("background-color", "white")])]

# 显示表格
st.table(df.style.set_table_styles(styles).set_properties(**{'position': 'sticky', 'top': '0'}))
