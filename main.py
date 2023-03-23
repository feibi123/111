import streamlit as st
import pandas as pd

# 创建示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie'] * 100,
        'Age': [18, 19, 20] * 100,
        'Gender': ['Female', 'Male', 'Male'] * 100}
df = pd.DataFrame(data)

# 设置表格样式
st.markdown(
    """
    <style>
        #mytable {
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
        }

        #mytable thead {
            position: sticky;
            top: 0;
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 显示表格
with st.beta_container():
    st.write("<div style='overflow-x: auto;'><table id='mytable'>", df.to_html(index=False), "</table></div>", unsafe_allow_html=True)

# 首行固定
st.markdown(
    """
    <script>
        var tableOffset = $("#mytable").offset().top;
        var $header = $("#mytable > thead").clone();
        var $fixedHeader = $("#header-fixed").append($header);
        
        $(window).bind("scroll", function() {
            var offset = $(this).scrollTop();
            if (offset >= tableOffset && $fixedHeader.is(":hidden")) {
                $fixedHeader.show();
            }
            else if (offset < tableOffset) {
                $fixedHeader.hide();
            }
        });
    </script>
    """,
    unsafe_allow_html=True
)

# 创建空的表格，用于显示固定的表头
st.markdown("<table id='header-fixed'></table>", unsafe_allow_html=True)

