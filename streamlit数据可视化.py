import streamlit as st
import pandas as pd
pd.set_option('display.max_colwidth', None)
st.set_page_config(layout="wide")

col1, col2 = st.sidebar.columns(2)
variable = col1.number_input("输入可变天数", min_value=16, max_value=60, value=31)  # 可变天数
variable2 = col2.number_input("输入安全库存", min_value=1, max_value=60, value=30)  # 30天安全库存
variable5 = col2.number_input("输入生产+物流周期", min_value=1, max_value=90, value=45)  # 物流周期
variable4 = col1.number_input("输入最小安全库存", min_value=1, max_value=45, value=20)  # 最小安全库存

uploaded_file = st.sidebar.file_uploader("上传订单报告", type="csv")
uploaded_file1 = st.sidebar.file_uploader("上传产品属性表", type="csv")  # 读取产品属性表
uploaded_file2 = st.sidebar.file_uploader("上传库存表", type="csv")

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

dt = pd.read_csv(uploaded_file2, header=0, encoding='gbk')
dt = dt.rename(columns={'Merchant SKU': 'sku'})
dt['Inbound'] = dt['Inbound'].astype(int)
dt['Available'] = dt['Available'].astype(int)
dt['FC transfer'] = dt['FC transfer'].astype(int)
dt = dt[(dt['Inbound'] != 0) | (dt['Available'] != 0) | (dt['FC transfer'] != 0)]
dt = dt.rename(columns={'Inbound': '在途库存数量'})
dt = dt.assign(在库库存数量=lambda x: x['Available'] + x['FC transfer'])
cols1 = ['sku', '在途库存数量', '在库库存数量']
dt = dt.reindex(columns=cols1)

df = pd.merge(df, dt, on='sku', how='outer')  # 将7天销量表格、15天销量表格、可变销量表格和在库在途库存表格合并

dc = pd.read_csv(uploaded_file1, header=0, encoding='gbk')
dc = dc[['产品类别', '颜色', 'sku']]  # 只保留链接名称、父ASIN和sku列

df = pd.merge(df, dc, on='sku', how='left')  # 将7天销量表格、15天销量表格、可变销量表格、在途库存表格、在库库存表格和产品属性表合并
df.fillna(0, inplace=True)  # 将所有空值替换为0

df['1次'] = (df['7天销量'] > 0).astype(int)  # 计算次数
df['2次'] = (df['15天销量'] > 0).astype(int)
df['3次'] = (df['可变销量'] > 0).astype(int)
df['次数'] = df['1次'] + df['2次'] + df['3次']
df['平均销量'] = (df['7天销量'] / 7 + df['15天销量'] / 15 + df['可变销量'] / variable) / df['次数']
df.loc[df['次数'] == 0, '平均销量'] = 0
df['在库预计可售天数'] = df['在库库存数量'] / df['平均销量']  # 计算在库预计可售天数
df.loc[df['次数'] == 0, '在库预计可售天数'] = 0

df['总预计可售天数'] = (df['在库库存数量'] + df['在途库存数量']) / df['平均销量']
# 计算总预计可售天数
df.loc[df['平均销量'] == 0, '总预计可售天数'] = 0

df['安全库存'] = df['平均销量'] * variable2  # 计算安全库存
df.loc[df['次数'] == 0, '安全库存'] = 0

df['最晚发货时间'] = round(df['总预计可售天数'] - variable5)  # 计算最晚发货时间

df['建议补货数量'] = df['平均销量'] * (variable5 + variable4 - df['总预计可售天数'])  # 计算建议补货数量


def fill_or_not(x):
    if x >= 0:
        return '是'
    else:
        return '否'


df['是否发货'] = df['建议补货数量'].apply(fill_or_not)

df[['7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量', '在库预计可售天数', '总预计可售天数', '安全库存', '建议补货数量', '最晚发货时间']] = \
    df[['7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量', '在库预计可售天数', '总预计可售天数', '安全库存',
        '建议补货数量', '最晚发货时间']].round().astype(int)  # 保留整数
cols = ['产品类别', '颜色', 'sku', '7天销量', '15天销量', '可变销量', '在途库存数量', '在库库存数量', '在库预计可售天数', '总预计可售天数', '安全库存',
        '最晚发货时间', '是否发货', '建议补货数量']
df = df.reindex(columns=cols)
df = df.drop(columns=['1次', '2次', '3次', '次数'], errors='ignore')

col1, col2 = st.columns(2)

link_names = df["产品类别"].unique()
link_names = ["全选"] + list(link_names)
selected_links = col1.multiselect("选择产品", link_names)

if "全选" in selected_links:
    df = df
else:
    df = df[df["产品类别"].isin(selected_links)]

link_names1 = df["是否发货"].unique()
link_names1 = ["全选"] + list(link_names1)
selected_links1 = col2.multiselect("是否发货", link_names1)

if "全选" in selected_links1:
    df = df
else:
    df = df[df["是否发货"].isin(selected_links1)]


def style_cell(x):
    style = ''
    if x < 30:
        style += "font-weight: bold; color: green;"
    elif x > 180:
        style += "font-weight: bold; color: red;"
    return style


# 设置单元格样式
def style_cell1(y):
    style = ''
    if y < 10:
        style += "font-weight: bold; color: red;"
    else:
        style += ""
    return style


# 应用样式
styled_df = df.style.applymap(style_cell1, subset=['最晚发货时间'])
styled_df = styled_df.applymap(style_cell, subset=['在库预计可售天数', '总预计可售天数'])
st.table(styled_df)
