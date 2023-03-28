import pandas as pd
import streamlit as st


def style_cell(x):
    if x < 80:
        return 'background-color: red'
    elif x > 90:
        return 'background-color: green'
    else:
        return ''

df = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/pythonexcel.xlsx')

styled_df = df.style.applymap(style_cell, subset=['语文', '英语'])

# Set the page configuration
st.set_page_config(layout="wide")

# Set the first row to be frozen
styled_df.set_sticky(axis='index')

# Display the styled DataFrame with a fixed height and width
st.dataframe(styled_df, height=600, width=None, max_height=800)
