import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 将第一行固定
st.markdown(
    """
    <style>
        /* 首行固定 */
        .scrollable-table > table > thead > tr {
            position: fixed;
            top: 0;
        }

        /* 第二行作为滚动条的起点 */
        .scrollable-table > table > tbody > tr:nth-child(2) {
            margin-top: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.write("<div class='scrollable-table'>", df.to_html(index=False), "</div>", unsafe_allow_html=True)
