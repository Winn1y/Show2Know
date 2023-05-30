import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

"""
    函数说明
    matplotlib.pyplot.scatter(  x, y, s=None, c=None, 
                                marker=None, cmap=None, 
                                norm=None, vmin=None, 
                                vmax=None, alpha=None, 
                                linewidths=None, verts=<deprecated parameter>, 
                                edgecolors=None, *, plotnonfinite=False, data=None, **kwargs )
    
    / x, y：         点的位置，x, y支持多维数组，但是x, y的维度必须一致，多维数组会被展平（flatten）为一维数组。
    / s：            标记的面积。默认值为rcParams['lines.markersize'] ** 2。
    / c：            标记的颜色。数组、颜色数组或颜色。 可选参数。
    /marker：        标记样式。取值参考matplotlib.markers。默认值为rcParams["scatter.marker"] ('o')。
    /cmap：          色彩映射。已注册的色彩映射名称或Colormap实例。默认值为rcParams["image.cmap"] ('viridis')。cmap只能在c参数为浮点数数组时才能使用。
    /norm：          Normalize，默认值为None。如果c参数为浮点数数组，norm参数在[0,1]范围内缩放颜色数据，c构造与cmap的颜色映射。如果为None，默认的colors.Normalize。
    /alpha：         浮点数。取值范围为[0,1]，0为透明，1为不透明。默认值为None。
    /linewidths：    标记边缘线宽。浮点数或类数组结构。默认值为rcParams["lines.linewidth"] (1.5)。
    /edgecolors：    标记边缘颜色。取值为{'face', 'none', None}、颜色、颜色序列。默认值为rcParams["scatter.edgecolors"] ('face')。
                     'face'：标记边缘颜色与标记颜色相同
                     'none'：没有边线。
"""

# input数据 X、Y 2维
x = [1.1, 2.3, 4.5, 8.8, 10]
y = [3.2, 0.1, 6.1, 9.9, 10]

# 参数
color = [100, 2, 3, 4, 5]
sizes = [30, 30, 30, 30, 30]
changecolor = colors.Normalize(vmin=10, vmax=100)
alpha = 0.3

"""
    show
"""
plt.scatter(x, y, c=color, s=sizes, alpha=alpha, cmap='viridis',norm=changecolor)
plt.colorbar()
plt.show()

