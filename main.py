import streamlit as st
import pandas as pd

# Create example data
data = {'Name': ['Alice', 'Bob', 'Charlie'] * 100,
        'Age': [25, 30, 35] * 100,
        'Gender': ['F', 'M', 'M'] * 100}
df = pd.DataFrame(data)

# Define CSS and JavaScript to freeze first row of table and synchronize scrolling with page
freeze_table_script = """
    <style>
        /* Add custom styles for first row */
        .freeze-table th:first-child, .freeze-table td:first-child {
            position: sticky;
            left: 0;
            z-index: 1;
            background-color: white;
        }
        /* Add custom styles for remaining rows */
        .freeze-table th, .freeze-table td {
            background-color: white;
        }
    </style>
    <script>
        // Synchronize scrolling of table with page
        window.onscroll = function() {
            var scrollPosition = window.pageYOffset;
            var tableTop = document.getElementById('table').getBoundingClientRect().top + window.pageYOffset;
            var tableBottom = tableTop + document.getElementById('table').clientHeight;
            var windowHeight = window.innerHeight;
            if (scrollPosition > tableTop - windowHeight/2 && scrollPosition < tableBottom - windowHeight/2) {
                document.getElementById('table').style.transform = 'translate(0px,' + (scrollPosition - tableTop + windowHeight/2) + 'px)';
            }
        };
    </script>
"""

# Display table with frozen first row and synchronized scrolling
with st.beta_container():
    st.markdown(freeze_table_script, unsafe_allow_html=True)
    st.table(df.style.set_table_attributes('class="freeze-table" id="table"').hide_index())

