import streamlit as st
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 在CSS中设置表格样式
st.markdown(
    """
    <style>
      /* 表格样式 */
      table {
        width: 100%;
        border-collapse: collapse;
      }

      /* 表头样式 */
      table th {
        position: sticky;
        top: 0;
        background-color: white;
        font-weight: bold;
      }

      /* 首列样式 */
      table th:first-child,
      table td:first-child {
        position: sticky;
        left: 0;
        background-color: white;
      }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
st.write(df)
