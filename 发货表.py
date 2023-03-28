import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# 创建数据
data = {'姓名': ['小明', '小红', '小张', '小李', '小刚'], '语文': [78, 92, 85, 90, 87], '数学': [83, 76, 92, 88, 82],
        '英语': [87, 85, 72, 90, 92]}
df = pd.DataFrame(data)

# 设置单元格样式
def style_cell(x):
    style = ''
    if x < 80:
        style += "font-weight: bold; color: red;"
    elif x > 90:
        style += "font-weight: bold; color: green;"
    return style

# 应用样式
styled_df = df.copy()
styled_df[['语文', '英语']] = df[['语文', '英语']].applymap(style_cell)

# 构建 GridOptions
gb = GridOptionsBuilder.from_dataframe(styled_df)
gb.configure_column("index", headerName="", maxWidth=50, lockPosition=True)
gb.configure_grid_options(domLayout='normal', widthMode='fit')

# 展示 AgGrid
gridOptions = gb.build()
grid = AgGrid(styled_df, gridOptions=gridOptions, height=600)

# 显示原始 DataFrame
st.write(df, wide=True)

