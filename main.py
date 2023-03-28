from st_aggrid import AgGrid
import pandas as pd

# 创建示例数据
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# 使用 AgGrid 组件展示数据
grid = AgGrid(df)
