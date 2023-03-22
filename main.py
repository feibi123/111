import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "产品类别": ["A", "A", "B", "C"],
    "是否发货": ["是", "否", "是", "否"],
    "销售数量": [20, 50, 180, 10]
})

st.set_page_config(layout="wide")
selected_links = st.multiselect("选择产品", df["产品类别"].unique())
selected_links1 = st.multiselect("是否发货", df["是否发货"].unique())

# 创建容器
container = st.beta_container()

# 在容器中放置复选框
with container:
    # 使用 CSS 样式表固定复选框的位置
    st.markdown("""
    <style>
    .st-ct {
        position: fixed !important;
        top: 100px;
        left: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.write(selected_links)
    st.write(selected_links1)

# 显示数据框
df = df[df["产品类别"].isin(selected_links) & df["是否发货"].isin(selected_links1)]
st.table(df)
