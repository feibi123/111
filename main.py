import streamlit as st
import pandas as pd
uploaded_file1 = st.sidebar.file_uploader("上传订单报告")
# 如果用户上传了文件
if uploaded_file1 is not None:
    # 读取文件内容
    content = uploaded_file1.read()

    # 尝试使用 utf-8 编码方式进行解码
    try:
        decoded_content = content.decode('utf-8')
    except UnicodeDecodeError:
        # 如果解码失败，则尝试使用 gbk 编码方式进行解码
        decoded_content = content.decode('gbk')
        
        

    # 将解码后的文件内容转换为 pandas 数据框
df = pd.read_csv(StringIO(decoded_content), skiprows=7)
    
st.write("""
<style>
    /* 冻结表格首行 */
    .freeze {
        position: sticky;
        top: 0;
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

st.table(df.head(20).style.set_table_attributes("class='freeze'"))
