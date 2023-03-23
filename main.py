import streamlit as st
import pandas as pd

# 创建示例数据
data = {'Name': ['小明', '小红', '小刚'] * 100,
        'Age': [18, 19, 20] * 100,
        'Gender': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 设置表格样式
st.markdown(
    """
    <style>
        .dataframe {
            position: fixed;
            top: 70px;
            width: 100%;
            height: 100%;
            z-index: 0;
            overflow: auto;
        }

        .dataframe thead {
            position: sticky;
            top: 0;
            background-color: white;
            z-index: 1;
        }

        .dataframe th {
            font-weight: bold;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.table(df)
