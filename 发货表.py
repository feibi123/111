import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder
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

# 创建 GridOptionsBuilder 对象，用于构建 AgGrid 的参数
gb = GridOptionsBuilder.from_dataframe(df)

# 冻结首行
gb.configure_grid_options(domLayout='normal')
gb.configure_column("index", headerName="", maxWidth=50, lockPosition=True)

gridOptions = gb.build()

# 使用 AgGrid 组件展示数据
grid = AgGrid(df, gridOptions=gridOptions, height=600)
