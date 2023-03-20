import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a CSV file", type="text/csv")

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    df = pd.read_csv(StringIO(content))
    st.write("File content:")
    st.write(df)
