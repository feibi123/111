import streamlit as st
import pandas as pd
from streamlit_aggrid import GridOptionsBuilder, AgGrid

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 创建 Ag-Grid 配置实例
gob = GridOptionsBuilder.from_dataframe(df)

# 设置列宽和行高
gob.configure_column("姓名", width=120)
gob.configure_column("年龄", width=80)
gob.configure_column("性别", width=80)
gob.configure_column("身高", width=80)
gob.configure_column("体重", width=80)

gob.configure_grid_options(domLayout='normal',
                           rowDragManaged=True,
                           enableRangeSelection=True,
                           enableCharts=True,
                           enableStatusBar=True,
                           enableFilter=True,
                           enableSorting=True,
                           enableColResize=True,
                           enableCellChangeFlash=True,
                           suppressDragLeaveHidesColumns=True,
                           rowSelection='single',
                           rowMultiSelectWithClick=True,
                           suppressRowClickSelection=False,
                           groupSelectsChildren=True,
                           groupSelectsFiltered=True,
                           suppressAggFuncInHeader=True,
                           suppressMultiSort=False,
                           rowHeight=22,
                           headerHeight=28,
                           defaultColDef={'sortable': True})

# 添加冻结首行
gob.configure_grid_options(floatingFilter=True, 
                           floatingTopRow=True, 
                           suppressHorizontalScroll=True, 
                           floatingTopRowData=df.head(1))

grid_response = AgGrid(df, gridOptions=gob.build(), height=500)

# 显示表格
st.write(grid_response['data'])
