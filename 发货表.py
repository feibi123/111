import pandas as pd
import streamlit as st

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 设置表格样式
table_style = """
<style>
table {
  table-layout: fixed;
}
thead {
  position: sticky;
  top: 0;
  background-color: white;
}
tbody {
  overflow-y: scroll;
  height: 400px;
}
th, td {
  text-align: center;
}
</style>
"""

# 显示表格
st.markdown(table_style, unsafe_allow_html=True)
st.markdown(df.to_html(index=False), unsafe_allow_html=True)
