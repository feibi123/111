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
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# 使用st.markdown函数添加HTML标记
st.markdown(
    """
    <style>
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

# 添加表格并将表头放置在一个固定的div元素中
with st.container():
    # 将表头放置在一个固定的div元素中
    st.markdown(
        f'<div class="freeze">{df.columns[0]}</div>',
        unsafe_allow_html=True
    )
    # 显示数据表格
    st.dataframe(df)
