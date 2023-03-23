import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 将表格铺满全屏
st.markdown(
    """
    <style>
        .scrollable-table {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 9999;
            overflow: auto;
        }

        .scrollable-table table {
            width: 100%;
        }

        /* 固定表头 */
        .scrollable-table thead th {
            position: sticky;
            top: 0;
            background-color: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.write("<div class='scrollable-table'>", df.to_html(index=False), "</div>", unsafe_allow_html=True)
