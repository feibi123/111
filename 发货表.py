import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

df = pd.DataFrame({
    'A': [1,2,3,4,5,6],
    'B': [11,22,33,44,55,66],
    'C': [11,22,33,44,55,66],
    'D': [11,22,33,44,55,66],
    'E': [11,22,33,44,55,66],
})

# 创建GridOptionsBuilder对象
gob = GridOptionsBuilder.from_dataframe(df)

# 设置表格首行冻结
gob.configure_grid_options(domLayout='normal', enableRangeSelection=True, enableCharts=True, enableStatusBar=True, enableFilter=True, enableSorting=True, enableColResize=True, enableCellChangeFlash=True, suppressDragLeaveHidesColumns=True, rowSelection='single', rowMultiSelectWithClick=True, suppressRowClickSelection=False, groupSelectsChildren=True, groupSelectsFiltered=True, suppressAggFuncInHeader=True, suppressMultiSort=False, rowHeight=22, headerHeight=28, defaultColDef={'sortable': True})

# 获取GridOptions对象
go = gob.build()

# 在st_aggrid函数中添加gridOptions参数
AgGrid(df, gridOptions=go, height=300)
