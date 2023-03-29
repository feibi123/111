import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

df = pd.DataFrame({
    'A': [1,2,3,4,5,6],
    'B': [11,22,33,44,55,66],
    'C': [11,22,33,44,55,66],
    'D': [11,22,33,44,55,66],
    'E': [11,22,33,44,55,66],
})

gob = GridOptionsBuilder.from_dataframe(df)

gob.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
gob.configure_grid_options(domLayout='normal', enableRangeSelection=True, enableCharts=True, enableStatusBar=True, enableFilter=True, enableSorting=True, enableColResize=True, enableCellChangeFlash=True, suppressDragLeaveHidesColumns=True, rowSelection='single', rowMultiSelectWithClick=True, suppressRowClickSelection=False, groupSelectsChildren=True, groupSelectsFiltered=True, suppressAggFuncInHeader=True, suppressMultiSort=False, rowHeight=22, headerHeight=28, defaultColDef={'sortable': True}, autoSizeColumns=True)

go = gob.build()

# 定义CSS样式
css = """
<style>
    #my-grid-wrapper {
        width: 100%;
        height: 100%;
        position: relative;
    }

    #my-grid {
        width: 100%;
        height: 100%;
        position: absolute;
    }
</style>
"""

# 在st.markdown函数中添加CSS样式和表格
st.markdown(css + '<div id="my-grid-wrapper"><div id="my-grid">' + AgGrid(df, gridOptions=go, height=300)._repr_html_() + '</div></div>', unsafe_allow_html=True)
