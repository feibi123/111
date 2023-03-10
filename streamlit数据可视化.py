import streamlit as st
import pandas as pd

pd.set_option('display.max_colwidth', None)
st.set_page_config(layout="wide")
col1, col2 = st.sidebar.columns(2)
variable = col1.number_input("输入可变天数", min_value=16, max_value=60, value=31)  # 可变天数
variable2 = col1.number_input("输入30天安全库存", min_value=1, max_value=30, value=30)  # 30天安全库存
variable5 = col2.number_input("输入物流周期", min_value=1, max_value=60, value=45)  # 物流周期
variable3 = col2.number_input("输入60天安全库存", min_value=31, max_value=60, value=60)  # 60天安全库存
variable4 = col1.number_input("输入最小安全库存", min_value=1, max_value=7, value=7)  # 最小安全库存

uploaded_file1 = st.sidebar.file_uploader("上传订单报告", type="csv")
uploaded_file = st.sidebar.file_uploader("上传库存表", type="txt")
uploaded_file3 = st.sidebar.file_uploader("上传产品属性表", type="csv")
df = pd.read_csv(uploaded_file1, header=None, encoding='gbk')  # header=None 参数禁止将第一行读入为列标题
df = df.drop(df.index[:7])  # 删除前7行
df.columns = df.iloc[0]  # 将第八行作为标题
df = df.drop(df.index[0])  # 删除第八行
df = df.dropna(subset=['quantity'])  # 删除含有空值的行
df['quantity'] = df['quantity'].astype(int)  # 将quantity列转换成整数类型
df = df.dropna(subset=['type'])  # 删除含有空值的行
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

dt = pd.read_csv(uploaded_file, delimiter='\t', header=0)
dt = dt.rename(columns={'Merchant SKU': 'sku'})
dt['Inbound'] = dt['Inbound'].astype(int)
dt['Available'] = dt['Available'].astype(int)
dt['FC transfer'] = dt['FC transfer'].astype(int)
dt = dt.rename(columns={'Inbound': '在途库存数量'})
dt['在库库存数量'] = round(dt['Available'] + dt['FC transfer'])
cols1 = ['sku', '在途库存数量', '在库库存数量']
dt = dt.reindex(columns=cols1)

df = pd.merge(df, dt, on='sku', how='outer')  # 将7天销量表格、15天销量表格、可变销量表格和在库在途库存表格合并

dc = pd.read_csv(uploaded_file3, header=0, encoding='gbk')  # 读取产品属性表，并将首行作为标题列
dc = dc[['产品类别', '颜色', 'sku']]  # 只保留产品类别和sku列
df = pd.merge(df, dc, on='sku', how='left')  # 将7天销量表格、15天销量表格、可变销量表格、在途库存表格、在库库存表格和产品属性表合并
df.fillna(0, inplace=True)  # 将所有空值替换为0
df['1次'] = (df['7天销量'] > 0).astype(int)  # 计算次数
df['2次'] = (df['15天销量'] > 0).astype(int)
df['3次'] = (df['可变销量'] > 0).astype(int)
df['次数'] = df['1次'] + df['2次'] + df['3次']
df['在库预计可售天数'] = df['在库库存数量'] * df['次数'] / (
            df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable)  # 计算在库预计可售天数
df.loc[df['次数'] == 0, '在库预计可售天数'] = 0
df['总预计可售天数'] = (df['在库库存数量'] + df['在途库存数量']) * df['次数'] / (
            df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable)
# 计算总预计可售天数
df.loc[df['次数'] == 0, '总预计可售天数'] = 0
df['安全库存'] = (
            (df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable) / df['次数'] * variable2)  # 计算安全库存
df.loc[df['次数'] == 0, '安全库存'] = 0
df['最晚发货时间'] = round((df['总预计可售天数'] - variable5))  # 计算最晚发货时间
df['最小安全库存'] = ((df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable) / df['次数'] * (
            variable4 + variable5))
# 计算最小安全库存
df.loc[df['次数'] == 0, '最小安全库存'] = 0
df['最小安全库存'] = round(df['最小安全库存'])  # 保留整数
df['建议补货数量'] = round((df['安全库存'] - df['在库库存数量']))  # 计算建议补货数量
df[['7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量', '在库预计可售天数', '总预计可售天数', '安全库存',
    '最晚发货时间', '最小安全库存', '建议补货数量']] \
    = df[['7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量', '在库预计可售天数',
          '总预计可售天数', '安全库存', '最晚发货时间', '最小安全库存', '建议补货数量']].round().astype(int)  # 保留整数
cols = ['产品类别', '颜色', 'sku', '7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量',
        '在库预计可售天数', '总预计可售天数', '安全库存',
        '最晚发货时间', '最小安全库存', '建议补货数量']
df = df.reindex(columns=cols)
df = df.drop(columns=['1次', '2次', '3次', '次数'], errors='ignore')
link_names = df["产品类别"].unique()
link_names = ["全选"] + list(link_names)
selected_links = st.multiselect("选择产品类别", link_names)
if "全选" in selected_links:
    df = df
else:
    df = df[df["产品类别"].isin(selected_links)]


def style_cell(x):
    style = ''
    if x < 30:
        style += "font-weight: bold; color: green;"
    elif x > 180:
        style += "font-weight: bold; color: red;"
    return style


df = df.style.applymap(style_cell, subset=['在库预计可售天数', '总预计可售天数'])
st.table(df)
