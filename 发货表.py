import streamlit.components.v1 as components
from st_aggrid import AgGrid
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 设置 defaultColumnDef 属性，使所有列名能够完全显示出来
default_column_def = {'minWidth': 50}
grid_options = {
    'defaultColumnDef': default_column_def
}

# 使用 AgGrid 组件展示数据
grid = AgGrid(df, grid_options=grid_options)
