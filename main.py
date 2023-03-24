from st_aggrid import GridOptionsBuilder, AgGrid
import streamlit as st
import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 32, 18]})

# 计算屏幕宽度的 90%
screen_width = st.experimental_get_query_params()['screenWidth'][0]
table_width = int(0.9 * float(screen_width))

# 创建 GridOptionsBuilder 对象
gb = GridOptionsBuilder.from_dataframe(df)

# 设置表格宽度
gb.with_grid_width(f"{table_width}px")

# 构建表格选项
go = gb.build()

# 使用 AgGrid 组件来呈现表格
AgGrid(df, gridOptions=go)
