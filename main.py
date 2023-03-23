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
        .freeze-table-wrapper {
            position: fixed;
            top: 0;
            width: 100%;
            height: 100%;
            overflow-x: hidden;
            overflow-y: auto;
        }

        .freeze-table {
            width: max-content;
            margin-top: 45px;
        }

        .freeze-table th {
            position: sticky;
            top: 0;
            background-color: white;
            z-index: 1;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.write("<div class='freeze-table-wrapper'>", "<table class='freeze-table'>", df.to_html(index=False), "</table>", "</div>", unsafe_allow_html=True)
