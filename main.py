import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid

# 创建一个包含随机数据的 DataFrame
df = pd.DataFrame({
    '姓名': ['小明', '小红', '小刚'] * 100,
    '年龄': [18, 19, 20] * 100,
    '性别': ['男', '女', '男'] * 100
})

# 创建一个 GridOptionsBuilder 对象并从 DataFrame 中获取选项
gb = GridOptionsBuilder.from_dataframe(df)
gb.column_types(col_age='numeric')
go = gb.build()
AgGrid(df, gridOptions=go)
AgGrid(df, gridOptions=go)
