import streamlit as st

data = [
    ['A1', 'B1', 'C1', 'D1', 'E1'],
    ['A2', 'B2', 'C2', 'D2', 'E2'],
    ['A3', 'B3', 'C3', 'D3', 'E3'],
    ['A4', 'B4', 'C4', 'D4', 'E4'],
    ['A5', 'B5', 'C5', 'D5', 'E5'],
    ['A6', 'B6', 'C6', 'D6', 'E6'],
    ['A7', 'B7', 'C7', 'D7', 'E7'],
    ['A8', 'B8', 'C8', 'D8', 'E8'],
    ['A9', 'B9', 'C9', 'D9', 'E9'],
    ['A10', 'B10', 'C10', 'D10', 'E10']
]

st.write('Frozen Columns with Scrollable Body')
left, right = st.beta_columns([1, 3])
with left:
    st.write('Column 1 (Frozen)')
with right:
    st.write('Columns 2-5 (Scrollable)')
    for row in data:
        col1, col2, col3, col4, col5 = st.beta_columns([1, 1, 1, 1, 1])
        col1.write(row[0])
        col2.write(row[1])
        col3.write(row[2])
        col4.write(row[3])
        col5.write(row[4])
