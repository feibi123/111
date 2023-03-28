import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

st.write("""
<style>
grid-container {
    height: 500px; /* 设置 AgGrid 的高度 */
    overflow: auto; /* 显示页面滚动条 */
}
grid-frozen-rows {
    position: sticky; /* 固定在顶部 */
    top: 0; /* 距离顶部的位置 */
}
</style>
""", unsafe_allow_html=True)

# 设置 AgGrid 组件的宽度
grid_options = {
    'width': '100%',
    'enableSorting': True, # 开启排序
    'enableFilter': True, # 开启过滤
    'enableColResize': True, # 开启调整列宽
    'floatingTopRow': True, # 启用冻结行
    'floatingTopRowData': [df.columns.tolist()], # 冻结首行
}

# 使用 AgGrid 组件展示数据
grid = AgGrid(df, grid_options=grid_options, key='grid')

# 如果您的数据集非常大，可以使用 pagination_mode='virtual' 来开启虚拟分页，以加速渲染速度
# grid = AgGrid(df, grid_options=grid_options, key='grid', pagination_mode='virtual')
