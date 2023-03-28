import streamlit as st
import pandas as pd

data = {
    '姓名': ['小明', '小红', '小张', '小李', '小刚'],
    '语文': [78, 92, 85, 90, 87],
    '数学': [83, 76, 92, 88, 82],
    '英语': [87, 85, 72, 90, 92]
}

df = pd.DataFrame(data)

st.write(df.style.highlight_max(axis=0))

# 冻结表头
st.write(df.style.highlight_max(axis=0).set_table_styles([{'selector': 'thead th', 'props': [('position', 'sticky'), ('top', '0px')]}]))

# 铺满全屏
st.write(df.style.set_table_styles([{'selector': 'table', 'props': [('width', '100%'), ('height', '100%')]}]))
