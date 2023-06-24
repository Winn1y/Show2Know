import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

"""
    官方样例demo1
    ps：输入已做修改统一
"""

r0 = 1.5
x = [0.1, 0.2, 2.1, 1.1, 0.7]
y = [0.8, 1.2, 3.4, 5.5, 1.1]
area = [196.20574417, 220.67150595, 201.23125343, 128.48019489, 382.42566283]
x = np.array(x)
y = np.array(y)
area = np.array(area)
c = np.sqrt(area)
area1 = np.ma.masked_where(x < r0, area)
area2 = np.ma.masked_where(x >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))
plt.show()

"""
    官方样例demo2
    ps：输入已做修改统一 
"""

data = {'a': [ 0, 1,2,5,10,15],
        'b': [10,20,5,1,20,40],
        'c': [ 1,20,5,5, 2,30],
        'd': [200,500,100,400,100,300]}

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

"""
    官方样例demo3
"""

# input数据 X、Y 2维
x = [1.1, 2.3, 4.5, 8.8, 10]
y = [3.2, 0.1, 6.1, 9.9, 10]

# 参数
color = [100, 2, 3, 4, 5]
sizes = [30, 30, 30, 30, 30]
changecolor = colors.Normalize(vmin=10, vmax=100)
alpha = 0.3

plt.scatter(x, y, c=color, s=sizes, alpha=alpha, cmap='viridis',norm=changecolor)
plt.colorbar()
plt.show()


