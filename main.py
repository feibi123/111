import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 冻结表格的首行
def freeze_table(df):
    # 获取表格HTML代码
    table_html = df.to_html(index=False, classes=['freeze'])
    # 在表格HTML代码中添加CSS样式
    styled_html = '<style>.freeze tbody tr:first-child {position: sticky; top: 0; background-color: white;}</style>' + table_html
    return styled_html

# 显示冻结首行的表格
st.write(freeze_table(df), unsafe_allow_html=True)
