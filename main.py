import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid

# 创建一个包含随机数据的 DataFrame
df = pd.DataFrame( {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100})

screen_width = st.experimental_get_query_params()['screenWidth'][0]
table_width = int(0.9 * float(screen_width))

# 创建一个 GridOptionsBuilder 对象并从 DataFrame 中获取选项
gb = GridOptionsBuilder.from_dataframe(df)

gb.with_grid_width(f"{table_width}px")

# 构建表格选项
go = gb.build()

# 使用 AgGrid 组件来呈现表格
AgGrid(df, gridOptions=go)
