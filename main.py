import streamlit as st
import pandas as pd

# 创建示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie'] * 100,
        'Age': [18, 19, 20] * 100,
        'Gender': ['Female', 'Male', 'Male'] * 100}
df = pd.DataFrame(data)

# 设置表格样式
st.markdown(
    """
    <style>
        #mytable thead {
            position: sticky;
            top: 0;
            background-color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.table(df)
