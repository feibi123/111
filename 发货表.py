import streamlit as st
import pandas as pd
from streamlit_aggrid import AgGrid

# 引入ag-Grid的JavaScript库
ag_grid_js = "https://unpkg.com/ag-grid-community/dist/ag-grid-community.min.noStyle.js"
st.markdown(f'<script src="{ag_grid_js}"></script>', unsafe_allow_html=True)

# 引入ag-Grid的CSS样式文件
ag_grid_css = "https://unpkg.com/ag-grid-community/dist/styles/ag-grid.css"
ag_theme_css = "https://unpkg.com/ag-grid-community/dist/styles/ag-theme-alpine.css"
st.markdown(f'<link rel="stylesheet" href="{ag_grid_css}">', unsafe_allow_html=True)
st.markdown(f'<link rel="stylesheet" href="{ag_theme_css}">', unsafe_allow_html=True)

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 10,
        '年龄': [18, 19, 20] * 10,
        '性别': ['男', '女', '男'] * 10,
        '城市': ['北京', '上海', '广州'] * 10,
        '分数': [80, 85, 90] * 10}
df = pd.DataFrame(data)

# 创建一个容器，用于呈现ag-Grid表格
grid_id = "myGrid"
grid_height = 500
st.markdown(f'<div id="{grid_id}" style="height: {grid_height}px; width: 100%;" class="ag-theme-alpine"></div>', unsafe_allow_html=True)

# 定义表格列
column_defs = [{"headerName": col, "field": col} for col in df.columns]

# 定义表格数据
row_data = df.to_dict('records')

# 初始化ag-Grid
grid_options = {
    "columnDefs": column_defs,
    "rowData": row_data,
    "enableSorting": True,
    "enableFilter": True,
    "enableColResize": True,
    "rowSelection": "multiple",
    "groupSelectsChildren": True,
    "suppressAggFuncInHeader": True,
    "pivotMode": True,
    "groupDefaultExpanded": 1,
    "autoGroupColumnDef": {"headerName": "城市", "field": "城市", "rowGroup": True},
    # 更多配置选项...
}
grid_response = AgGrid(grid_data=df, grid_options=grid_options, height=grid_height, width='100%', return_mode='AS_INPUT', key=grid_id)

# 处理用户的表格操作
if grid_response['event_type'] == 'GridOptionsChanged':
    df = pd.DataFrame(grid_response['data'])
    st.dataframe(df)

# 显示数据总结
st.write(f"共有{len(df)}行数据。")

# 显示筛选后的结果
if grid_response['selected_rows']:
    selected_data = pd.DataFrame(grid_response['selected_rows'])
    st.write(f"共有{len(selected_data)}行数据被选中：")
    st.dataframe(selected_data)
else:
    st.write("未选择任何数据。")
