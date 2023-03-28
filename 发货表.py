from st_aggrid import GridOptionsBuilder, AgGrid

import pandas as pd

# 创建示例数据
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# 创建 GridOptionsBuilder 对象
gb = GridOptionsBuilder.from_dataframe(df)

# 配置 GridOptions
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_side_bar()

# 使用 AgGrid 组件展示数据
grid = AgGrid(df, gridOptions=gb.build(), width='100%', height='400px')
