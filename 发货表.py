import pandas as pd
import streamlit as st

# 创建示例数据
data = {'姓名': ['小明', '小红', '小刚'] * 100,
        '年龄': [18, 19, 20] * 100,
        '性别': ['男', '女', '男'] * 100,
        '身高': ['男', '女', '男'] * 100,
        '体重': ['男', '女', '男'] * 100}
df = pd.DataFrame(data)

# 在 Streamlit 中显示表格，并将表格全屏并冻结首行
st.markdown("""
    <style>
        /* 让表格全屏 */
        .fullScreenFrameWrapper {
            width: 100%;
        }
        /* 冻结首行 */
        .freeze-table-row th {
            position: sticky;
            top: 0;
            background: white;
            z-index: 1;
        }
        /* 将表格添加滚动条 */
        .freeze-table-container {
            max-height: 500px;
            overflow-y: auto;
        }
    </style>
""", unsafe_allow_html=True)

# 使用 CSS 类 "freeze-table-row" 和 "freeze-table-container" 实现首行冻结和添加滚动条
st.table(df.style.set_table_attributes('class="freeze-table-row"').set_properties(
    **{'width': '100%'}).set_table_styles(
    [{"selector": ".freeze-table-row", "props": [("position", "relative")]}]
).render()).container.set_attributes('class="freeze-table-container"')
