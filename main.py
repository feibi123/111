import streamlit as st
import pandas as pd

# 创建示例数据
data = {'Name': ['John', 'Emily', 'Michael'] * 100,
        'Age': [25, 30, 35] * 100,
        'Gender': ['M', 'F', 'M'] * 100}
df = pd.DataFrame(data)

# 显示表格
with st.beta_container():
    # 设置表格样式
    st.markdown(
        """
        <style>
            .scrollable-table {
                position: fixed;
                top: 80px;
                left: 0;
                width: 100%;
                height: calc(100% - 80px);
                z-index: 9999;
                overflow: auto;
            }

            .scrollable-table table {
                width: 100%;
            }
            
            .scrollable-table thead th {
                position: sticky;
                top: 0;
                background-color: white;
            }
            
            .scrollable-table thead th:first-child {
                left: 0;
                z-index: 1;
            }
            
            .scrollable-table thead th:nth-child(2) {
                left: 120px;
            }
            
            .scrollable-table thead th:nth-child(3) {
                left: 200px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.write("<div class='scrollable-table'>", df.iloc[1:].to_html(index=False), "</div>", unsafe_allow_html=True)

    # 显示表头
    st.write("<div class='scrollable-table'>", df.iloc[:1].to_html(index=False), "</div>", unsafe_allow_html=True)

