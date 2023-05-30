import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 生成随机数据
np.random.seed(0)
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(1, 1, 1000)
data3 = np.random.normal(2, 1, 1000)

# 创建数据框
df = pd.DataFrame({'Group 1': data1, 'Group 2': data2, 'Group 3': data3})

# 绘制Joy Plot
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.kdeplot(data=df, fill=True, palette="husl")
plt.xlabel("Value")
plt.ylabel("Density")
plt.title("Joy Plot of Random Data")
plt.show()
