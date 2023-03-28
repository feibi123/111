import streamlit as st
import pandas as pd

df = pd.read_excel("E:\发货表\FSM\1.xlsx")

# 冻结表格首行
st.write(
    df.style
    .set_table_styles([{'selector': 'thead', 'props': [('sticky', 'top')]}])
    .set_properties(**{'width': '100%', 'max-width': '100%'})
)

# 铺满全屏
st.markdown("""
    <style>
        .fullScreen {
            height: 100vh !important;
        }
    </style>
""", unsafe_allow_html=True)

