# import streamlit as st

# st.write("<style>.title{position: fixed; top: 0; left: 0; width: 100%; padding: 80px 0; background-color: #fff; text-align: center; font-size: 36px; font-weight: bold; z-index: 1;}</style>", unsafe_allow_html=True)
# st.write("<div class='title'>这是一个大标题</div>", unsafe_allow_html=True)

# st.write("<div style='margin-top: 100px; z-index: 0;'>这是一的撒发文件的文件的境况章。</div>")

import streamlit as st

# 冻结大标题和上传文件组件
st.set_page_config(page_title="My Page", page_icon=":sunglasses:", layout="wide", initial_sidebar_state="collapsed")

# 设置大标题
st.title("My Title")

# 添加上传文件组件
uploaded_file = st.file_uploader("Choose a file")

# 创建一个滚动区域来显示文本
with st.beta_container():
    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed et ligula euismod, consequat dolor vel, rhoncus nibh. In semper gravida massa, ac eleifend mi ultrices a. Integer vitae diam sed mauris auctor fermentum. Fusce euismod neque vel turpis consectetur, in consectetur nisi rhoncus. Vestibulum vestibulum semper odio, a lacinia ex accumsan et. In hac habitasse platea dictumst. Sed tristique ex vel imperdiet blandit. Quisque posuere lectus lacus, eget iaculis ante feugiat in. Aliquam placerat quam id metus euismod, non ultrices nunc iaculis. Aliquam luctus nisi quam, ut elementum enim sagittis at. "
    st.markdown(f"<div style='height: 500px; overflow-y: scroll;'>{lorem_ipsum}</div>", unsafe_allow_html=True)
