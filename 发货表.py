import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Column 1': ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'sed', 'do'],
    'Column 2': ['Ut', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris'],
    'Column 3': ['Duis', 'aute', 'irure', 'dolor', 'in', 'reprehenderit', 'in', 'voluptate', 'velit', 'esse'],
    'Column 4': ['Cillum', 'dolore', 'eu', 'fugiat', 'nulla', 'pariatur', 'excepteur', 'sint', 'occaecat', 'cupidatat'],
    'Column 5': ['Non', 'proident', 'sunt', 'in', 'culpa', 'qui', 'officia', 'deserunt', 'mollit', 'anim']
})

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

#table-container {
    height: 300px;
    overflow: auto;
    position: relative;
}

#table-container table {
    position: absolute;
    top: 0;
    left: 0;
    background-color: #fff;
    z-index: 1;
}

#table-container th:first-child {
    position: sticky;
    top: 0;
    background-color: #fff;
    z-index: 2;
}
"""

js = """
$(function() {
  var tableContainer = $('#table-container');
  tableContainer.scroll(function() {
    var scrollLeft = tableContainer.scrollLeft();
    $('th:first-child', tableContainer).css('left', scrollLeft);
  });
});
"""

def main():
    # Write CSS and JS to page
    st.write(f'<style>{css}</style>', unsafe_allow_html=True)
    st.write(f'<script>{js}</script>', unsafe_allow_html=True)

    # Write table to page
    st.write(f'<div id="table-container">{df.to_html(index=False, header=True)}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    
