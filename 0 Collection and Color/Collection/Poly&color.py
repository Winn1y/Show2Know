import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

# 创建一些示例数据
data = np.random.rand(10, 10)  # 10x10 的示例数据
fig, ax = plt.subplots()

# 准备多边形的顶点坐标（示例数据，实际应用中需要提供多边形的坐标）
vertices = []
for i in range(10):
    for j in range(10):
        vertices.append([(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)])

# 创建一个 PolyCollection 对象
pc = PolyCollection(vertices, edgecolors='k')

# 标准化数据并设置颜色映射
# 这里示例数据范围在0到1之间，因此不需要标准化
# 如果数据范围不同，可以使用 Normalize 进行标准化
pc.set_array(data.ravel())  # 设置颜色数据

ax.add_collection(pc)
# 设置坐标轴范围
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
# 添加颜色条
cbar = plt.colorbar(pc, ax=ax)
cbar.set_label('Values')
ax.set_title('PolyCollection with Color Mapping')
plt.show()
