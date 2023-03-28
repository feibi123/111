import streamlit as st
import pandas as pd
import streamlit_aggrid as st_ag

# 创建一个包含随机数据的数据框
df = pd.DataFrame(np.random.randn(100, 5), columns=['col1', 'col2', 'col3', 'col4', 'col5'])

# 在 Streamlit 应用中显示表格
st_ag.grid(df, height=500, theme='streamlit', frozen_rows=1)
