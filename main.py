import streamlit as st
import codecs

def read_uploaded_file(file):
    with codecs.open(file, 'r', encoding=codecs.lookup(file.name).name) as f:
        file_contents = f.read()
    return file_contents

def main():
    st.title("文件上传示例")
    uploaded_files = st.file_uploader("上传文件", type=["txt", "csv"])
    if uploaded_files is not None:
        file_data = []
        for file in uploaded_files:
            file_dict = {"name": file.name, "content": file.read()}
            file_data.append(file_dict)

        for file in file_data:
            st.write(f"文件名：{file['name']}")
            st.write(f"文件内容：{read_uploaded_file(file['content'])}")

if __name__ == "__main__":
    main()
