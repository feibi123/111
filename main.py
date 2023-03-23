import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 定义 CSS 样式
st.markdown(
    """
    <style>
        /* 设置表格样式 */
        .scrollable-table {
            height: 400px;
            overflow-y: scroll;
        }
        /* 设置表头样式 */
        .scrollable-table th {
            position: sticky;
            top: 0;
            background-color: white;
        }
        /* 设置首行样式 */
        .scrollable-table tbody tr:first-child {
            position: sticky;
            top: 0;
            background-color: white;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
st.table(df.style.set_table_attributes('class="scrollable-table"').render())
