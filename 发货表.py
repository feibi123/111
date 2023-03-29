# import streamlit as st

# st.write("<style>.title{position: fixed; top: 0; left: 0; width: 100%; padding: 80px 0; background-color: #fff; text-align: center; font-size: 36px; font-weight: bold; z-index: 1;}</style>", unsafe_allow_html=True)
# st.write("<div class='title'>这是一个大标题</div>", unsafe_allow_html=True)

# st.write("<div style='margin-top: 100px; z-index: 0;'>这是一的撒发文件的文件的境况章。</div>")

import streamlit as st

# 冻结上传文件按钮和大标题
st.set_page_config(page_title="My Page", page_icon=":sunglasses:", layout="wide")

# 设置大标题
st.title("My Title")

# 创建一些示例文本
lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id dictum quam. Suspendisse mollis sagittis enim sit amet molestie. Vivamus ullamcorper sapien vitae risus rutrum ultrices. Proin bibendum, eros non dignissim consectetur, nisi tellus auctor tellus, et pharetra turpis enim vel dui. Nam id libero mi. Nullam porta congue euismod. Sed vel eleifend nunc. Donec iaculis ullamcorper nunc id pulvinar. Sed tristique efficitur lorem, id volutpat lacus interdum nec. Proin at turpis nunc. Proin imperdiet consequat eros non tristique. Ut elementum, turpis a lacinia convallis, odio enim pretium lorem, sit amet laoreet elit tellus vel elit. Donec in varius sapien, vel aliquam nisl. """

# 创建一个滚动区域来显示文本
with st.beta_container():
    st.markdown(f"<div style='height: 500px; overflow-y: scroll;'>{lorem_ipsum}</div>", unsafe_allow_html=True)
