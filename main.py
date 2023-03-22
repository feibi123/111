import streamlit as st

st.write("# My Streamlit App")

# 在页面中固定一个块
st.write("## Fixed Block")

# 在页面中固定两个复选框
st.write('<div style="position: fixed; top: 50px; left: 50px;">')
selected_links = st.multiselect("选择产品", ["产品1", "产品2", "产品3"])
selected_links1 = st.multiselect("是否发货", ["是", "否"])
st.write('</div>')

# 显示一些示例内容
st.write("## Example Content")
st.write("This is some example content.")
st.write("This is more example content.")
st.write("This is even more example content.")

