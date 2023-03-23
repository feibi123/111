import pandas as pd
from IPython.core.display import display, HTML

# 生成示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank'],
        'Age': [25, 32, 18, 47, 22, 19],
        'Gender': ['F', 'M', 'M', 'M', 'F', 'M']}
df = pd.DataFrame(data)

# 设置表格样式
style = """
<style>
table {
    border-collapse: collapse;
    width: 100%;
    table-layout: fixed;
}

th {
    position: sticky;
    top: 0;
    background-color: white;
}

th, td {
    border: 1px solid black;
    padding: 10px;
    text-align: center;
}
</style>
"""

# 生成HTML代码并输出
html = style + df.to_html(index=False)
display(HTML(html))
