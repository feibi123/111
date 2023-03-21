import pandas as pd
import streamlit as st

def read_csv_file(uploaded_file):
    # 读取上传的 CSV 文件
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"读取文件失败：{e}")
        return None
    
    return df

def freeze_table_header(df):
    # 将数据框的第一行作为表头，并将其从数据框中删除
    header = df.iloc[0]
    df = df[1:]

    # 使用 set_index() 方法将表头转换为行索引
    df = df.set_index(header)

    # 显示上传文件的按钮
    uploaded_file = st.file_uploader("上传文件")

    # 在显示的表格上方添加一个新的表格，其中只有一行，该行的值与原始数据框的表头相同
    new_table = st.empty()
    new_table.add_rows(1)
    new_table[0, :].data = header

    # 显示数据框，此时表头已经成为了行索引
    table = st.table(df)

    # 将上传文件的按钮、新表格和原始表格合并
    merged_table = f"{uploaded_file} {new_table._get_value()}\n{table._get_value()}"
    table._update_html(merged_table)

# 主程序
st.set_page_config(page_title="冻结表头和上传文件", layout="wide")

# 显示页面标题和说明文本
st.title("冻结表头和上传文件")
st.write("这是一个示例页面，用于演示如何冻结表头并上传文件。")

# 显示上传文件的按钮，并读取文件内容
uploaded_file = st.file_uploader("选择要上传的文件", type="csv")
if uploaded_file is not None:
    df = read_csv_file(uploaded_file)
    if df is not None:
        # 冻结表头并显示数据框
        freeze_table_header(df)
