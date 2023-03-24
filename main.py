import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid

# 创建一个包含随机数据的 DataFrame
df = pd.DataFrame({'姓名': ['小明', '小红', '小刚'] * 100,
                   '年龄': [18, 19, 20] * 100,
                   '性别': ['男', '女', '男'] * 100})

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

# 设置表格的宽度和高度
gb.with_dimensions(height=500, width='100%')

# 首行冻结
gb.with_row_style(rowStyle={"border-top": "1px solid black", "font-weight": "bold"}, rowHeight=35)

# 构建表格选项
go = gb.build()

# 使用 AgGrid 组件来呈现表格
st.header("数据表格")
with st.spinner('正在加载数据，请稍等...'):
    AgGrid(df, gridOptions=go)
