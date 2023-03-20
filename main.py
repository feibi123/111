import streamlit as st

def read_file(file):
    content = file.read()
    encoding = detect_encoding(content[:100]) # 只读取文件的前100字节用于判断编码
    return content.decode(encoding)

def detect_encoding(bytes_content):
    if bytes_content.startswith(b'\xef\xbb\xbf'): # UTF-8 with BOM
        return 'utf-8-sig'
    elif bytes_content[0] == 0xb5 and bytes_content[1] == 0xc7: # GB2312
        return 'gb2312'
    else:
        return 'utf-8'

uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file is not None:
    file_contents = read_file(uploaded_file)
    st.write(file_contents)

