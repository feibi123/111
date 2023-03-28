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

th,
td {
    padding: 8px;
    border: 1px solid #ddd;
    text-align: left;
}

tbody {
    overflow-y: auto;
    height: 200px;
}
"""

# Set up JavaScript code to fix the first row of the table
javascript = """
const table = document.querySelector('table');
const tbody = table.querySelector('tbody');
const firstRow = tbody.querySelector('tr');

function fixTableHeader() {
  if (window.scrollY > table.offsetTop) {
    firstRow.classList.add('fixed');
  } else {
    firstRow.classList.remove('fixed');
  }
}

window.addEventListener('scroll', fixTableHeader);
"""

def main():
    # Write CSS to page
    st.write(f'<style>{css}</style>', unsafe_allow_html=True)

    # Write table to page
    st.write(df.to_html(index=False, header=True), unsafe_allow_html=True)

    # Write JavaScript to page
    st.write(f'<script>{javascript}</script>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

