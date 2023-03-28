import streamlit.components.v1 as components
from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
from io import StringIO
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

grid_options = {
    'columnDefs': [{'field': col, 'sortable': True} for col in df.columns],
    'rowSelection': 'single',
    'floatingFilter': True,  # 冻结首行
    'ensureDomOrder': True,  # 优化渲染性能
    'enableFilter': True,
    'enableSorting': True,
    'enableColResize': True,
    'enableRangeSelection': True,
    'pagination': True,
    'paginationAutoPageSize': True,
    'suppressMenuFilterPanel': True,
    'suppressContextMenu': True,
    'domLayout': 'normal',  # 设置为normal模式
    'overlayNoRowsTemplate': '没有数据',
}

grid_width = len(df.columns) * 200  # 根据列数计算表格宽度

with st.spinner('正在加载数据...'):grid = AgGrid(
        df,
        gridOptions=grid_options,
        width=grid_width,
        theme='light',
        allow_unsafe_jscode=True,  # 允许渲染JS代码，防止组件出错
    )

st.markdown("<style>div.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)
