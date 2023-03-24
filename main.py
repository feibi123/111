import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid

# 创建一个包含随机数据的 DataFrame
df = pd.DataFrame({
    '姓名': ['小明', '小红', '小刚'] * 100,
    '年龄': [18, 19, 20] * 100,
    '性别': ['男', '女', '男'] * 100
})

# 创建一个 GridOptionsBuilder 对象并从 DataFrame 中获取选项
gb = GridOptionsBuilder.from_dataframe(df)

# 配置表格选项
gb.configure_default_column(
    groupable=True,
    value=True,
    enableRowGroup=True,
    aggFunc='sum',
    editable=True
)

# 构建表格选项
go = gb.build()

# 获取屏幕宽度
screen_width = st.experimental_get_query_params().get('screenWidth', [None])[0]

# 设置表格宽度
if screen_width:
    go.with_dimensions(width=screen_width)
else:
    go.with_full_width()

# 使用 AgGrid 组件来呈现表格
AgGrid(df, gridOptions=go)
