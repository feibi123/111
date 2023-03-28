import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Column 1': ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'sed', 'do']*100,
    'Column 2': ['Ut', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris']*100,
    'Column 3': ['Duis', 'aute', 'irure', 'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 'velit', 'esse']*100,
    'Column 4': ['Cillum', 'dolore', 'eu', 'fugiat', 'nulla', 'pariatur', 'excepteur', 'sint', 'occaecat', 'cupidatat']*100,
    'Column 5': ['Non', 'proident', 'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 'anim']*100
})

# Set up CSS styles for the table
css = """
table {
    width: 100%;
    border-collapse: collapse;
}

th {
    position: fixed;
    top: 0;
    background-color: white;
    z-index: 1;
}

th,
td {
    padding: 8px;
    border: 1px solid #ddd;
    text-align: left;
}

tbody {
    overflow-y: auto;
    height: 200px;
    margin-top: 40px;
}

::-webkit-scrollbar {
    width: 5px;
}

::-webkit-scrollbar-track {
    background-color: #f1f1f1;
}

::-webkit-scrollbar-thumb {
    background-color: #888;
    border-radius: 5px;
}
"""

def main():
    # Write CSS to page
    st.write(f'<style>{css}</style>', unsafe_allow_html=True)

    # Write table to page
    st.table(df)

if __name__ == "__main__":
    main()
