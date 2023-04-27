import pandas as pd
import glob

# 指定文件夹路径
folder_path = "E:/广告表/广告"

# 读取文件夹中的所有CSV文件
all_files = glob.glob(os.path.join(folder_path, "*.csv"))
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

# 打印合并后的DataFrame
print(df)
