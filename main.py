import streamlit as st
import pandas as pd
import os

# 创建上传文件夹的函数
def folder_upload():
    uploaded_folder = st.file_uploader("选择文件夹", type=["zip", "tar"])
    if uploaded_folder is not None:
        # 将文件夹解压缩到本地文件夹
        with open(os.path.join("temp", uploaded_folder.name), "wb") as f:
            f.write(uploaded_folder.getbuffer())
        st.success(f"{uploaded_folder.name} 已上传")
        return True
    else:
        return False

# 创建合并CSV文件的函数
def merge_csv():
    # 获取temp文件夹中的所有CSV文件
    csv_files = [f for f in os.listdir("temp") if f.endswith(".csv")]
    # 如果temp文件夹中没有CSV文件，则返回
    if len(csv_files) == 0:
        st.warning("没有找到CSV文件")
        return
    # 将所有CSV文件合并成一个数据帧
    dfs = []
    for file in csv_files:
        df = pd.read_csv(os.path.join("temp", file))
        dfs.append(df)
    merged_df = pd.concat(dfs, ignore_index=True)
    # 将合并后的数据帧转换成字符串并打印在网页上
    st.write(merged_df.to_string(index=False))

# 创建一个Streamlit应用程序
def main():
    # 创建一个上传文件夹的按钮
    if folder_upload():
        # 如果成功上传文件夹，则创建一个合并CSV文件的按钮
        if st.button("合并CSV文件"):
            merge_csv()

if __name__ == "__main__":
    main()
