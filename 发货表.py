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

# 设置 AgGrid 组件的宽度
grid_options = {
    'width': '100%',
    'enableRangeSelection': True,
    'enableFilter': True,
    'enableSorting': True,
    'floatingTopRow': True,
    'floatingTopRowData': [df.columns.tolist()],
    'floatingTopRowStyle': {'zIndex': '1', 'fontWeight': 'bold'}
}

# 使用 AgGrid 组件展示数据
grid_response = AgGrid(df, gridOptions=grid_options)

# 输出表格数据
if 'data' in grid_response:
    st.write(grid_response['data'])
