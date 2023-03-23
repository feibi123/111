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
        .freeze-row::-webkit-scrollbar {
            display: none;
        }
        .freeze-row {
            position: sticky;
            top: 0;
            z-index: 1;
        }
        .freeze-row th {
            background-color: white !important;
            position: -webkit-sticky;
            position: sticky;
            top: 0;
        }
        .freeze-row td {
            background-color: white !important;
        }
        .full-width {
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.table(df.style.set_table_attributes('class="freeze-row full-width"').hide_index())
