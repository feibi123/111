import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
# 创建示例数据
data = {'姓名nananananannanananananannanananananannananan': ['小明nanananananannana', '小红', '小刚'] * 100,
        '年nananananananananan龄': [18, 19, 20] * 100,
        '性nananananan别': ['男nananananananananananananannananananananananannanananan', '女', '男'] * 100,
        '身nanannanananananananannananananannanaanan高': ['男', '女', '男'] * 100,
        '体anananananananananannananananananannananannananannananananan重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

gb = GridOptionsBuilder.from_dataframe(df)
# 设置页面宽度和高度
st.set_page_config(page_title="AgGrid Example", layout="wide")

# 设置 AgGrid 组件的属性
gridOptions = gb.build()
gridOptions['domLayout'] = 'normal'
gridOptions['defaultColDef'] = {'flex': 1}
gridOptions['onFirstDataRendered'] = 'function(params) {params.api.sizeColumnsToFit(); params.api.autoSizeColumns();}'
gridOptions['columnDefs'][0]['width'] = 100
gridOptions['columnDefs'][1]['width'] = 100

window_height = st.experimental_get_query_params().get('height', [None])[0]

if window_height:
    window_height = int(window_height.replace('px', ''))
else:
    window_height = None  # 设置一个默认值


window_width = '100%'
# 使用 AgGrid 组件展示数据
grid_response = AgGrid(df, gridOptions=gridOptions, height=window_height, width='100%')
# grid_response = AgGrid(df, gridOptions=gridOptions, height=600, width='100%')          
