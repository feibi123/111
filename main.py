import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚', '小红', '小刚', '小红', '小刚', '小红', '小刚', '小红', '小刚', '小红', '小刚', '小红', '小刚'],
        '年龄': [18, 19, 20, 18, 19, 20, 18, 19, 20, 18, 19, 20, 18, 19, 20],
        '性别': ['男', '女', '男', '男', '女', '男', '男', '女', '男', '男', '女', '男', '男', '女', '男']}
df = pd.DataFrame(data)

# 冻结第一行的样式
styles = [dict(selector="th", props=[("font-size", "150%"),
                                     ("text-align", "center"),
                                     ("color", "white"),
                                     ("background-color", "#4CAF50")])]
styled_table = df.style.set_properties(**{'text-align': 'center'}).set_table_styles(styles)

# 将样式应用于整个表格
st.write(styled_table)
