import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode

# 创建一个 GridOptionsBuilder 对象
gb = GridOptionsBuilder.from_dataframe(df)

# 设置表格高度和宽度
gb.configure_default_column(
    groupable=True,
    value=True,
    enableRowGroup=True,
    aggFunc='sum',
    editable=True
)

# 构建表格选项
go = gb.build()

# 使用 AgGrid 组件来呈现表格
AgGrid(df, gridOptions=go, height=500, width=800)
