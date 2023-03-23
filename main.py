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
        #my_table td:first-child {
            position: -webkit-sticky;
            position: sticky;
            left: 0;
            z-index: 1;
            background-color: white;
        }
        #my_table thead th {
            background-color: white;
        }
        .fullscreen {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            width: 100%;
            height: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.write("<div class='fullscreen'><table id='my_table' class='scrollable-table'>", df.to_html(index=False), "</table></div>", unsafe_allow_html=True)
