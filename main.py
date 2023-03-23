import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚', '小红', '小刚', '小红', '小刚', '小红', '小刚', '小红', '小刚', '小红', '小刚', '小红', '小刚'],
        '年龄': [18, 19, 20, 18, 19, 20, 18, 19, 20, 18, 19, 20, 18, 19, 20],
        '性别': ['男', '女', '男', '男', '女', '男', '男', '女', '男', '男', '女', '男', '男', '女', '男']}
df = pd.DataFrame(data)

# 设置表格样式
st.markdown(
    """
    <style>
        .scrollable-table {
            height: 300px;
            overflow: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.write("<div class='scrollable-table'>", df.to_html(index=False), "</div>", unsafe_allow_html=True)
