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
        .scrollable-table-container {
            position: fixed;
            top: 50px;
            left: 0;
            right: 0;
            bottom: 0;
            overflow-y: auto;
        }

        .scrollable-table-container table {
            width: 100%;
        }

        .scrollable-table-container td, .scrollable-table-container th {
            white-space: nowrap;
        }

        .fixed-table {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1;
        }

        .fixed-table thead tr {
            position: sticky;
            top: 0;
        }

        .fixed-table th {
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 分离表头和数据
header = df.iloc[:1]
data = df.iloc[1:]

# 显示表格
with st.beta_container():
    # 固定表头
    st.write("<div class='fixed-table'>", header.to_html(index=False), "</div>", unsafe_allow_html=True)

    # 可滚动数据
    st.write("<div class='scrollable-table-container'>", data.to_html(index=False), "</div>", unsafe_allow_html=True)
