import streamlit as st
import streamlit_aggrid as st_ag
import pandas as pd

df = pd.DataFrame({
   'name': ['Alice', 'Bob', 'Charlie', 'David'],
   'age': [25, 32, 18, 47],
   'city': ['New York', 'Paris', 'London', 'Tokyo'],
   'country': ['USA', 'France', 'UK', 'Japan']
})

grid_height = 500
st_ag.grid(df, height=grid_height, fit_columns_on_grid_load=True)
