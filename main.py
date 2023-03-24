import pandas as pd
from st_aggrid import GridOptionsBuilder

# 创建一个包含随机数据的 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})

# 创建一个 GridOptionsBuilder 对象并从 DataFrame 中获取选项
gb = GridOptionsBuilder.from_dataframe(df)

# 配置表格选项
gb.configure_default_column(
    groupable=True,
    value=True,
    enableRowGroup=True,
    aggFunc='sum',
    editable=True
)

# 构建表格选项
go = gb.build()

# 使用 AgGrid 组件来呈现表格
AgGrid(df, gridOptions=go)
