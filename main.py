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
        .scrollable-table {
            position: fixed;
            top: 150px;
            left: 0;
            right: 0;
            bottom: 0;
            overflow-y: auto;
        }

        .scrollable-table table {
            width: 100%;
        }

        .scrollable-table thead {
            position: sticky;
            top: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.write("<div class='scrollable-table'>", df.to_html(index=False), "</div>", unsafe_allow_html=True)
