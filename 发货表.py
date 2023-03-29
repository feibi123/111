import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
# st.set_page_config(page_title="AgGrid Example", layout="wide")
# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 创建 GridOptionsBuilder 对象
gb = GridOptionsBuilder.from_dataframe(df)

# 设置 AgGrid 组件的属性
gridOptions = gb.build()
gridOptions['onGridReady'] = "function(params) {params.api.setDomLayout('normal');params.api.sizeColumnsToFit();}"
gridOptions['defaultColDef'] = {'flex': 1}

# 使用 AgGrid 组件展示数据
# grid_response = AgGrid(df, gridOptions=gridOptions, height=600, width='100%')
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
gridOptions['onGridReady'] = "function(params) {params.api.setDomLayout('normal');params.api.sizeColumnsToFit();}"
gridOptions['defaultColDef'] = {'flex': 1}

# 使用 AgGrid 组件展示数据
window_height = st.experimental_get_query_params().get('height', [None])[0]


if window_height:
    window_height = int(window_height.replace("px", ""))
else:
    window_height = 300  # 如果没有设置高度，默认设置为 600 像素


st.markdown("""<style>body::-webkit-scrollbar{width: 10px;height: 10px;}</style>""", unsafe_allow_html=True)
grid_response = AgGrid(df, gridOptions=gridOptions, height=window_height, width='100%')
            
