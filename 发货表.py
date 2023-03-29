import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 设置页面宽度和高度
st.set_page_config(page_title="AgGrid Example", layout="wide")

# 创建 GridOptionsBuilder 对象
gb = GridOptionsBuilder.from_dataframe(df)

# 设置 AgGrid 组件的属性
gridOptions = gb.build()
gridOptions['enablePagination'] = True  # 启用分页功能
gridOptions['paginationAutoPageSize'] = True  # 自动调整每页显示的行数
gridOptions['onGridReady'] = "function(params) {params.api.setDomLayout('normal');}"

# 使用 AgGrid 组件展示数据
grid_response = AgGrid(df, gridOptions=gridOptions, height=600, width='100%')
