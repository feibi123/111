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

gb = GridOptionsBuilder.from_dataframe(df)
gridOptions = gb.build()
gridOptions['onGridReady'] = "function(params) {params.api.setDomLayout('normal');params.api.sizeColumnsToFit();}"
# gridOptions['defaultColDef'] = {'flex': 1}
window_height = st.experimental_get_query_params().get('height', [None])[0]
if window_height:
    window_height = int(window_height.replace('px', ''))
else:
    window_height = None  # 设置一个默认值
    
window_width = '100%'
gridOptions['columnDefs'] = [
    {'headerName': '姓名', 'field': '姓名', 'flex': 1},
    {'headerName': '年龄', 'field': '年龄', 'width': 110}, 'cellStyle': lambda params: {'color': 'red', 'fontWeight': 'bold'} if params.value < 10 else {}},
    {'headerName': '性别', 'field': '性别', 'flex': 1},
    {'headerName': '身高', 'field': '身高', 'width': 85},
    {'headerName': '体重', 'field': '体重', 'width': 92},
]

grid_response = AgGrid(df, gridOptions=gridOptions, height=window_height, width='100%')
