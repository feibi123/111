import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 将DataFrame转换为Styler对象，并添加CSS样式
styled_df = df.style.set_table_styles([{
    'selector': 'thead th',
    'props': [('position', 'sticky'), ('top', '0'), ('background-color', 'white')]
}])

# 在Streamlit中显示表格
st.table(styled_df)
