import pandas as pd
import streamlit as st
from io import StringIO
from streamlit.elements import layout_utils
from streamlit.proto import BlockPath_pb2

def set_block_container_style(display="flex"):
    """Set CSS style attributes to make elements flex and sticky"""
    st.markdown(
        f"""
        <style>
            #root {{
                display: {display};
            }}
            .stBlockContainer {{
                flex: 1;
            }}
            .streamlit-sticky.sticky-header {{
                top: 0px;
                z-index: 10000;
                position: sticky !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    
 set_block_container_style()
# 读取上传的文件
uploaded_file = st.file_uploader("Choose a file")

# 如果用户上传了文件
if uploaded_file is not None:
    # 读取文件内容
    content = uploaded_file.read()

    # 尝试使用 utf-8 编码方式进行解码
    try:
        decoded_content = content.decode('utf-8')
    except UnicodeDecodeError:
        # 如果解码失败，则尝试使用 gbk 编码方式进行解码
        decoded_content = content.decode('gbk')

    # 将解码后的文件内容转换为 pandas 数据框
    df = pd.read_csv(StringIO(decoded_content), skiprows=7)
    
    set_block_container_style(display="block")
    block = layout_utils.empty()
    block_path = BlockPath_pb2.BlockPath(path=[block.id])
    block.stickyHeaders = [block_path]
    block.stickyFooters = [block_path]

    # Display the data frame
    st.dataframe(df)
