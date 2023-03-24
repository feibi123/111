import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid

# 创建一个包含随机数据的 DataFrame
df = pd.DataFrame({'姓名': ['小明', '小红', '小刚'] * 100,
                   '年龄': [18, 19, 20] * 100,
                   '性别': ['男', '女', '男'] * 100})

# 创建一个 GridOptionsBuilder 对象并从 DataFrame 中获取选项
gb = GridOptionsBuilder.from_dataframe(df)

# 配置表格选项
gb.configure_column("姓名", minWidth=100)
gb.configure_column("年龄", minWidth=100)
gb.configure_column("性别", minWidth=100)

# 设置默认行高和列宽
gb.default_column_def(width=100)
gb.default_row_height(30)

# 构建表格选项
go = gb.build()

# 使用 AgGrid 组件来呈现表格
AgGrid(df, gridOptions=go, height=500)
