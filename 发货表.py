import streamlit as st
import pandas as pd

data = {
    '姓名': ['小明', '小红', '小张', '小李', '小刚'],
    '语文': [78, 92, 85, 90, 87],
    '数学': [83, 76, 92, 88, 82],
    '英语': [87, 85, 72, 90, 92]
}

df = pd.DataFrame(data)

# 设置单元格样式
def style_cell(x):
    if isinstance(x, (int, float)):
        if x < 80:
            style += "font-weight: bold; color: red;"
        elif x > 90:
             style += "font-weight: bold; color: green;"
        return style

# 应用样式
df = df.style.applymap(style_cell)

# 冻结首行
df.set_table_styles([{
    'selector': 'thead th',
    'props': [
        ('border', '1px solid #ccc'),
        ('font-size', '14px'),
        ('background-color', '#f8f9fa'),
        ('font-weight', 'bold'),
        ('text-align', 'center')
    ]
}]).set_properties(**{
    'text-align': 'center',
    'border': '1px solid #ccc',
    'font-size': '14px'
})

# 设置表格的宽度自适应页面的宽度
st.set_page_config(layout="wide")

# 将表格放入容器中，并使用 CSS 样式控制容器高度和滚动条
with st.beta_container():
    st.dataframe(df, height=400, width=1000)

    st.write(
        f"""<style>
        .css-1aumxhk {{
            max-height: 400px !important;
            overflow-y: scroll;
        }}
        </style>""",
        unsafe_allow_html=True,
    )
