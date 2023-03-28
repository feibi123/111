import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, AgGridTheme
import pandas as pd
import streamlit as st
from io import StringIO
pd.set_option('display.max_colwidth', None)
st.set_page_config(layout="wide")

uploaded_file1 = st.sidebar.file_uploader("上传订单报告")
df = pd.DataFrame()


# 如果用户上传了文件
if uploaded_file1 is not None:
    # 读取文件内容
    content = uploaded_file1.read()

    # 尝试使用 utf-8 编码方式进行解码
    try:
        decoded_content = content.decode('utf-8')
    except UnicodeDecodeError:
        # 如果解码失败，则尝试使用 gbk 编码方式进行解码
        decoded_content = content.decode('gbk')

    # 将解码后的文件内容转换为 pandas 数据框
    df = pd.read_csv(StringIO(decoded_content), skiprows=7)

    
df = df.dropna(subset=['quantity'])  # 删除含有空值的行
df['quantity'] = df['quantity'].astype(int)  # 将quantity列转换成整数类型
df = df.dropna(subset=['type'])   # 删除含有空值的行

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=False, sortable=True, resizable=True, filter=True)
gb.configure_grid_options(domLayout='normal')
gb.configure_pagination()
gb.configure_side_bar()
gb.configure_selection('single')
gridOptions = gb.build()

# 将 GridOptions 传递给 AgGrid 组件
grid_response = components.declare_component(
    "streamlit_aggrid",
    url="http://localhost:3001",
    path=st._RELEASE_INFO["componentPath"],
    version=st._RELEASE_INFO["componentVersion"],
)
with st.spinner('正在加载数据...'):
    component_value = grid_response(gridOptions=gridOptions, rowData=df.to_dict('records'), theme='ag-theme-alpine-dark', enable_enterprise_modules=False, key="ag")
    
# 从组件响应中获取 AgGrid 组件的状态
if component_value.get("selected_rows"):
    selected_rows = component_value["selected_rows"]
else:
    selected_rows = []
    
    
# 更新原始数据框以反映所选行
df_selected = pd.DataFrame(selected_rows)

# 使用 AgGrid 组件展示数据
grid = AgGrid(df_selected, height=500, width='100%', gridOptions=gridOptions, theme='ag-theme-alpine-dark', update_mode=GridUpdateMode.SELECTION_CHANGED, fit_columns_on_grid_load=True, allow_unsafe_jscode=True, key="ag")
