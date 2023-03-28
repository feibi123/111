import streamlit.components.v1 as components
from st_aggrid import AgGrid
import pandas as pd

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 使用 AgGrid 组件展示数据
grid = AgGrid(df)

# 将表格宽度铺满全屏
components.html(
    """
    <style>
    #root div:first-child {
        width: 100%;
    }
    </style>
    """
)
