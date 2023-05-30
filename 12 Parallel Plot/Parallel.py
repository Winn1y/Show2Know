import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成随机数据
np.random.seed(0)
data = np.random.rand(20, 4)

# 创建数据框
df = pd.DataFrame(data, columns=['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4'])

# 绘制平行坐标图
plt.figure(figsize=(10, 6))
pd.plotting.parallel_coordinates(df, 'Feature 1', colormap='cool')
plt.xlabel('Features')
plt.ylabel('Value')
plt.title('Parallel Coordinates Plot')
plt.legend(loc='upper right')
plt.show()
