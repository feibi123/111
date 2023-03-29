# import streamlit as st

# st.write("<style>.title{position: fixed; top: 0; left: 0; width: 100%; padding: 80px 0; background-color: #fff; text-align: center; font-size: 36px; font-weight: bold; z-index: 1;}</style>", unsafe_allow_html=True)
# st.write("<div class='title'>这是一个大标题</div>", unsafe_allow_html=True)

# st.write("<div style='margin-top: 100px; z-index: 0;'>这是一的撒发文件的文件的境况章。</div>")

import streamlit as st

# 添加上传文件按钮和大标题
# uploaded_file = st.file_uploader("上传文件")
st.markdown('<h1 id="title" style="position:fixed; top:0; left:0; right:0; background-color:#FFFFFF; z-index:999;">这是一个大标题</h1>', unsafe_allow_html=True)

# 添加正文内容
st.write("这里是正文一的撒发文件的文件的境一的撒发文件的文件的境一的撒发文件的文件的境一的撒发文件的文件的境一的撒发文件的文件的境内容...")
