import streamlit as st
import pandas as pd
import chardet

# Define function to detect file encoding
def detect_encoding(file):
    with open(file, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

# Create file uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if file is uploaded
if uploaded_file is not None:
    # Get file encoding
    file_encoding = detect_encoding(uploaded_file)
    # Read file based on encoding
    if file_encoding == 'utf-8':
        df = pd.read_csv(uploaded_file)
    elif file_encoding == 'GB2312':
        df = pd.read_csv(uploaded_file, encoding='GB18030')
    else:
        st.error("File encoding not supported")
    # Show data
    st.write(df)
else:
    st.info("Please upload a CSV file.")
