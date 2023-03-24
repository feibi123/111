import pandas as pd
from st_aggrid import GridOptionsBuilder, GridOptions, AgGrid

# 创建一个包含随机数据的 DataFrame
df = pd.DataFrame({'姓名': ['小明', '小红', '小刚'] * 100,
                   '年龄': [18, 19, 20] * 100,
                   '性别': ['男', '女', '男'] * 100})

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

# 使用屏幕宽度设置表格宽度
screen_width = st.experimental_get_query_params().get('screenWidth', [None])[0]
if screen_width:
    gb.configure_grid_options(domLayout='autoHeight',
                              enableBrowserTooltips=True,
                              with_full_width=False,
                              with_dimensions=True,
                              heightViewport='window.innerHeight',
                              widthViewport='{}.toString() + "px"'.format(screen_width),
                              rowHeight=32)

# 创建 GridOptions 对象
go_dict = gb.build()
go = GridOptions(**go_dict)

# 使用 AgGrid 组件来呈现表格
AgGrid(df, gridOptions=go, width='100%')
