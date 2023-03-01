import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    variable = st.number_input("输入可变天数", min_value=16, max_value=60, value=31)  # 可变天数
with col2:
    variable2 = st.number_input("输入30天安全库存", min_value=1, max_value=30, value=30)  # 30天安全库存
with col3:
    variable3 = st.number_input("输入60天安全库存", min_value=31, max_value=60, value=60)  # 60天安全库存
with col4:
    variable4 = st.number_input("输入最小安全库存", min_value=1, max_value=7, value=7)  # 最小安全库存
with col5:
    variable5 = st.number_input("输入物流周期", min_value=1, max_value=60, value=45)  # 物流周期

col7, col8, col9, col10 = st.columns(4)
with col7:
    uploaded_file = st.file_uploader("上传订单报告", type="csv")
df = pd.read_csv(uploaded_file, header=None, encoding='gbk')  # header=None 参数禁止将第一行读入为列标题
df = df.drop(df.index[:7])  # 删除前7行
df.columns = df.iloc[0]  # 将第八行作为标题
df = df.drop(df.index[0])  # 删除第八行
df = df.dropna(subset=['quantity'])  # 删除含有空值的行
df['quantity'] = df['quantity'].astype(int)  # 将quantity列转换成整数类型
df = df.dropna(subset=['type'])   # 删除含有空值的行
df = df[df['type'].str.contains('Order')]  # 从type列筛选出Order
df = df[['date/time', 'sku', 'quantity']]  # 只保留 'date/time', 'sku', 'quantity' 三列的内容
df = df.rename(columns={'date/time': 'datetime'})  # 将date/time列名更改为datetime
df['datetime'] = df['datetime'].str.extract(r'(\w{3} \d+, \d{4})')  # 用正则表达式提取出日期
df['datetime'] = pd.to_datetime(df['datetime'], format='%b %d, %Y')  # 转换列类型
df['datetime'] = df['datetime'].dt.date  # 保留年月日

df7 = df[df['datetime'] >= (df['datetime'].max() - pd.Timedelta(days=6))]  # 截取近7天的数据
df7 = df7.groupby(['sku'])['quantity'].sum().reset_index()  # 汇总近7天的数据
df7 = df7.rename(columns={'quantity': '7天销量'})  # 将’quantity‘列名改成’7天销量‘

df15 = df[df['datetime'] >= (df['datetime'].max() - pd.Timedelta(days=14))]  # 截取近15天的数据
df15 = df15.groupby(['sku'])['quantity'].sum().reset_index()  # 汇总近15天的数据
df15 = df15.rename(columns={'quantity': '15天销量'})  # 将’quantity‘列名改成’15天销量‘

dfv = df[df['datetime'] >= (df['datetime'].max() - pd.Timedelta(days=variable - 1))]  # 截取变量的数据
dfv = dfv.groupby(['sku'])['quantity'].sum().reset_index()  # 汇总变量的数据
dfv = dfv.rename(columns={'quantity': '可变销量'})  # 将’quantity‘列名改成’可变销量‘

df = pd.merge(df7, df15, on='sku', how='outer')  # 将7天销量表格和15天销量表格合并
df = pd.merge(df, dfv, on='sku', how='outer')  # 将7天销量表格、15天销量表格和可变销量表格合并

with col8:
    uploaded_file1 = st.file_uploader("上传在途库存", type="csv")  # 读取在途库存，并将首行作为标题列
dt = pd.read_csv(uploaded_file1, header=0)

with col9:
    uploaded_file2 = st.file_uploader("上传即时库存", type="csv")
dk = pd.read_csv(uploaded_file2, header=0, encoding='gbk')   # 读取即时库存，并将首行作为标题列
mask = (dk['detailed-disposition'] == 'SELLABLE') & (dk['country'] != 'CA')  # 筛选出'SELLABLE'和美国的在库库存
dk = dk.loc[mask]
dk = dk.groupby('sku')['quantity'].sum().reset_index()  # 汇总
dk = dk.rename(columns={'quantity': '在库库存数量'})  # 将’quantity‘列名改成’在库库存数量‘

df = pd.merge(df, dt, on='sku', how='outer')  # 将7天销量表格、15天销量表格、可变销量表格和在途库存表格合并
df = pd.merge(df, dk, on='sku', how='outer')  # 将7天销量表格、15天销量表格、可变销量表格、在途库存表格和在库库存表格合并

with col10:
    uploaded_file3 = st.file_uploader("上传产品属性表", type="csv")  # 读取产品属性表，并将首行作为标题列
dc = pd.read_csv(uploaded_file3, header=0)
dc = dc[['链接名称', '父ASIN', 'sku']]  # 只保留链接名称、父ASIN和sku列

df = pd.merge(df, dc, on='sku', how='left')  # 将7天销量表格、15天销量表格、可变销量表格、在途库存表格、在库库存表格和产品属性表合并
df.fillna(0, inplace=True)  # 将所有空值替换为0

df['1次'] = (df['7天销量'] > 0).astype(int)  # 计算次数
df['2次'] = (df['15天销量'] > 0).astype(int)
df['3次'] = (df['可变销量'] > 0).astype(int)
df['次数'] = df['1次'] + df['2次'] + df['3次']
df['在库预计可售天数'] = df['在库库存数量'] * df['次数'] / (df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable)  # 计算在库预计可售天数
df.loc[df['次数'] == 0, '在库预计可售天数'] = 0

df['总预计可售天数'] = (df['在库库存数量'] + df['在途库存数量']) * df['次数'] / (df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable)
# 计算总预计可售天数
df.loc[df['次数'] == 0, '总预计可售天数'] = 0

df['安全库存'] = ((df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable) / df['次数'] * variable2)  # 计算安全库存
df.loc[df['次数'] == 0, '安全库存'] = 0

df['最晚发货时间'] = round((df['总预计可售天数'] - variable5))  # 计算最晚发货时间

df['最小安全库存'] = ((df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable) / df['次数'] * (variable4 + variable5))
# 计算最小安全库存
df.loc[df['次数'] == 0, '最小安全库存'] = 0
df['最小安全库存'] = round(df['最小安全库存'])  # 保留整数

df['建议补货数量'] = round((df['安全库存'] - df['在库库存数量']))  # 计算建议补货数量
df[['7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量', '在库预计可售天数', '总预计可售天数', '安全库存', '最晚发货时间', '最小安全库存', '建议补货数量']] \
    = df[['7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量', '在库预计可售天数',
          '总预计可售天数', '安全库存', '最晚发货时间', '最小安全库存', '建议补货数量']].round().astype(int)  # 保留整数

cols = ['链接名称', '父ASIN', 'sku', '7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量', '在库预计可售天数', '总预计可售天数', '安全库存',
        '最晚发货时间', '最小安全库存', '建议补货数量']
df = df.reindex(columns=cols)
df = df.drop(columns=['1次', '2次', '3次', '次数'], errors='ignore')
link_names = df["链接名称"].unique()
link_names = ["全选"] + list(link_names)
selected_links = st.multiselect("选择链接名称", link_names)

if "全选" in selected_links:
    df = df
else:
    df = df[df["链接名称"].isin(selected_links)]


def style_cell(x):
    style = ''
    if x < 30:
        style += "font-weight: bold; color: green;"
    elif x > 180:
        style += "font-weight: bold; color: red;"
    return style


df = df.style.applymap(style_cell, subset=['在库预计可售天数', '总预计可售天数'])

st.dataframe(df)
