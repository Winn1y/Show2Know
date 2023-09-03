import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection
from matplotlib.collections import RegularPolyCollection

# PolyCollection
# 创建一些多边形的顶点坐标
polygons = [
    np.array([[1, 1], [2, 3], [4, 3], [3, 1]]),
    np.array([[5, 1], [6, 3], [8, 3], [7, 1]]),
    np.array([[2, 4], [4, 4], [3, 6]]),
]
scales=np.array([1,0.5,2])
facecolor_p=['r','g','b','pink']
poly_collection = PolyCollection(polygons,
                                 sizes=scales,
                                 edgecolor='black',
                                 facecolor=facecolor_p,
                                 linewidths=1)

# RegularPolyCollection
# 创建一些示例点云数据
num_points = 1000
x = np.random.rand(num_points) * 10  # 生成随机的 x 坐标
y = np.random.rand(num_points) * 10  # 生成随机的 y 坐标
sizes = np.random.rand(num_points) * 50  # 随机大小
colors = np.random.rand(num_points, 3)  # 随机颜色
# 创建 RegularPolyCollection
regular_polygons = RegularPolyCollection(
    numsides=6,  # 规则多边形的边数
    rotation=0,
    sizes=(50,),#也可以调整为sizes，随机大小
    edgecolor='b',
    facecolor=colors,
    linewidths=1,
    offsets=np.column_stack((x, y)),  # 点的坐标
    transOffset=plt.gca().transData,
)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].add_collection(poly_collection)
axes[0].set_xlim(1, 20)
axes[0].set_ylim(1,30)
axes[0].set_title('PolyCollection')
axes[0].set_xlabel('X-axis')
axes[0].set_ylabel('Y-axis')

axes[1].add_collection(regular_polygons)
axes[1].set_title('RegularPolyCollection')
axes[1].set_xlim(1, 10)
axes[1].set_ylim(1, 10)
axes[1].set_xlabel('X-axis')
axes[1].set_ylabel('Y-axis')
plt.show()
