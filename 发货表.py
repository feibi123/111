import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 创建 GridOptionsBuilder 对象
gob = GridOptionsBuilder.from_dataframe(df)

# 固定表格首行
gob.configure_default_column(groupable=False, value=True, enableRowGroup=True, aggFunc='sum', editable=True, resizable=True, filter=True, sortable=True, flex=1)
gob.configure_grid_options(domLayout='normal', rowDragManaged=True, enableRangeSelection=True, enableCharts=True, enableStatusBar=True, enableFilter=True, enableSorting=True, enableColResize=True, enableRangeSelection=True, enableCharts=True, enableStatusBar=True, enableFilter=True, enableSorting=True, enableColResize=True, enableCellChangeFlash=True, suppressDragLeaveHidesColumns=True, rowSelection='single', rowMultiSelectWithClick=True, suppressRowClickSelection=False, groupSelectsChildren=True, groupSelectsFiltered=True, suppressAggFuncInHeader=True, suppressMultiSort=False, rowHeight=22, headerHeight=28, defaultColDef={'sortable': True})

# 在页面上显示表格
grid_result = AgGrid(df, gridOptions=gob.build(), width='100%', height='500px', theme='streamlit', update_mode=GridUpdateMode.VALUE_CHANGED)

# 获取用户所做的更改
changed_df = grid_result['data']

# 输出更改后的结果
st.write(changed_df)
