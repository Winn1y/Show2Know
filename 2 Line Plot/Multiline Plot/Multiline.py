# -*- coding: utf-8 -*-

from math import sin
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
X,X2, Y ,Z = [], [], [], []
for x in np.linspace(0, 6*np.pi, 100):
    X.extend([x, x, None]),
    X2.extend([x+0.5, x+0.5, None]),
    Y.extend([0, sin(x), None]) 
    Z.extend([0, 0.5*sin(x)+0.5, None])  # 计算并存储 sin(2x) 的数据点
    #第三个元素是 None，以便 matplotlib 知道在两个数据点之间不连线

ax.plot(X, Y, color='lightblue', linewidth=2) #调整线宽与颜色
#ax.plot(X2, Z, color='black', linewidth=2)
plt.show()