import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 显示标题行
st.write(df.columns.tolist())

# 设置表格样式
st.markdown(
    """
    <style>
        #freeze-table thead {
            position: sticky;
            top: 0;
            z-index: 1;
            background-color: white;
        }
        #freeze-table tbody {
            height: 400px;
            overflow-y: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
st.write(
    df.style
        .set_table_attributes('id="freeze-table"')
        .set_properties(**{'width': '100%', 'text-align': 'center'})
        .set_table_styles([{'selector': 'th', 'props': [('font-weight', 'bold')]}])
        .hide_index()
)
