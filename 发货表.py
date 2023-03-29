import pandas as pd
import streamlit as st

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 设置表头固定
styles = [dict(selector="thead", props=[("position", "sticky"), ("top", "0px")])]

# 使用 Styler 将 DataFrame 转化为 HTML 格式
html = df.style.set_table_styles(styles).render()

# 渲染 HTML 字符串
st.markdown(html, unsafe_allow_html=True)
