import os
import chardet
import pandas as pd
import zipfile
from io import BytesIO
import streamlit as st

# 上传zip文件
uploaded_file = st.file_uploader("上传zip文件", type="zip")

if uploaded_file is not None:
    # 尝试解压缩上传的 ZIP 文件
    try:
        with zipfile.ZipFile(BytesIO(uploaded_file.read())) as zip_file:
            zip_file.extractall()
    except Exception as e:
        st.write(f"Error: {e}")

    # 读取文件内容
    content = uploaded_file.read()

    # 解压文件
    with zipfile.ZipFile(BytesIO(content)) as zip_file:
        zip_file.extractall()

    # 获取所有CSV文件，并检测编码方式
    csv_files = [file_name for file_name in os.listdir() if file_name.endswith('.csv')]
    csv_encodings = {}
    for file in csv_files:
        with open(file, 'rb') as f:
            result = chardet.detect(f.read())
            csv_encodings[file] = result['encoding']

    # 读取所有CSV文件并合并到一个数据框中
    df_list = []
    for file in csv_files:
        sheet_name = os.path.splitext(os.path.basename(file))[0]  # 获取文件名作为sheet名
        encoding = csv_encodings[file]
        df = pd.read_csv(file, encoding=encoding,
                         usecols=['SKU', '会话次数 – 移动应用', '会话次数 – 移动应用 – B2B', '会话次数 – 浏览器', '会话次数 – 浏览器 – B2B',
                                  '已订购商品数量', '已订购商品数量 - B2B'])
        df['日期'] = sheet_name  # 添加日期列
        df_list.append(df)
        print(f"File {file} loaded, {len(df)} rows.")

    print(f"Found {len(csv_files)} CSV files.")
    print(f"Loaded {len(df_list)} data frames.")
    
    if df_list:
        df = pd.concat(df_list, ignore_index=True)
        st.write(df)
    else:
        st.write("No CSV files found or loaded.")
st.write(content)
