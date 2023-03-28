import streamlit.components.v1 as components
from st_aggrid import AgGrid, AgGridTheme, GridOptionsBuilder
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

# 创建 grid options 对象并进行设置
grid_options = GridOptionsBuilder(). \
    row_selection('multiple'). \
    row_multi_select_with_click(True). \
    hide_columns(['id']). \
    enable_pagination(True). \
    enable_floating_filter(True). \
    enable_range_selection(True). \
    enable_column_virtualization(True). \
    enable_filter(True). \
    enable_sorting(True). \
    enable_cell_edit(False). \
    build()

# 设置 AgGrid 组件的主题为 FLAT，并且冻结首行
theme = AgGridTheme.FLAT
with st.spinner('正在加载数据...'):
    grid = AgGrid(df, gridOptions=grid_options, theme=theme, height=500, width='100%', allow_unsafe_jscode=True, 
                  on_ready='this.api.setPinnedTopRow(0)')

# 设置表格宽度与页面宽度一致
st.markdown(
     f"""
        <style>
            .fullWidth {{
                width: 100% !important;
            }}
        </style>
    """,
    unsafe_allow_html=True
)
