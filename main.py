# import streamlit as st
# import pandas as pd
# uploaded_file1 = st.sidebar.file_uploader("上传订单报告")
#  # 将解码后的文件内容转换为 pandas 数据框
# df = pd.read_csv(uploaded_file1, skiprows=7)
# df = df.dropna(subset=['quantity'])

# st.table(df)
import streamlit as st
import pandas as pd

# 创建示例数据
data = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
        'B': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
        'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
        'd': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
        'f': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
       }
df = pd.DataFrame(data)

st.markdown(
    """
    <style>
        /* 将表格的高度设置为100% */
        .full-height {
            height: 100%;
        }
        /* 将表格固定在页面的位置 */
        .fixed-table {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            overflow: auto;
        }
        /* 设置表头的位置为固定 */
        .freeze {
            position: sticky;
            top: 0;
            z-index: 1;
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示数据表格
st.markdown(
    f'<div class="fixed-table"><table class="full-height"><thead><tr class="freeze"><th>{df.columns[0]}</th></tr></thead><tbody>{df.to_html(index=False)}</tbody></table></div>',
    unsafe_allow_html=True
)
