import pandas as pd
import streamlit as st

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 设置表头固定和滚动
st.markdown("""
    <style>
    .freeze-table {
      overflow: auto;
      max-height: 600px;
    }
    .freeze-table thead {
      position: sticky;
      top: 0;
      background-color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.table(df.style.set_properties(**{'width': '100%', 'max-height': '500px', 'overflow-y': 'auto'}).set_table_attributes("class='freeze-table'"))
