import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 定义CSS样式
css = """
<style>
table.dataframe {
    width: 100%;
    border-collapse: collapse;
}

table.dataframe th {
    position: sticky;
    top: 0;
    background: white;
    border: 1px solid #d3d3d3;
    text-align: center;
    padding: 5px 0;
}

table.dataframe th:first-child {
    left: 0;
    z-index: 1;
}

table.dataframe td {
    border: 1px solid #d3d3d3;
    text-align: center;
    padding: 5px 0;
}

div.stTableContainer {
    height: 600px;
    overflow-y: scroll;
}

</style>
"""

# 显示数据
st.markdown(css, unsafe_allow_html=True)
st.table(df)
