import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 设置表格样式
st.markdown(
    """
    <style>
        /* 设置表格样式 */
        .scrollable-table {
            height: 600px;
            overflow-y: scroll;
            position: sticky;
            top: 0;
            background-color: white;
            z-index: 1;
        }

        /* 设置表头样式 */
        .scrollable-table th {
            position: sticky;
            top: 0;
            background-color: white;
            z-index: 2;
        }

        /* 设置表格行的样式 */
        .scrollable-table tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.write("<div class='scrollable-table'>", df.to_html(index=False), "</div>", unsafe_allow_html=True)
    
