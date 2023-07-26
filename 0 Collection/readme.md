Matplotlib.Collections.Collection

Collection 是 Matplotlib 中表示图形元素集合的基类。它是其他集合类（如 PathCollection、LineCollection、PolyCollection 等）的父类，并提供了一些共用的方法和属性。通常情况下，你不会直接使用 Collection 类，而是使用其子类来创建特定类型的集合。
类
matplotlib.collections.·(*, edgecolors=None, facecolors=None, linewidths=None, linestyles='solid', capstyle=None, joinstyle=None, antialiaseds=None, offsets=None, offset_transform=None, norm=None, cmap=None, pickradius=5.0, hatch=None, urls=None, zorder=1, **kwargs) 
方法
set_transform()：设置集合的坐标变换对象。
set_offset_position()：设置集合的偏移位置。
get_offset_position()：获取集合的偏移位置。
set_offset_position_fraction()：设置集合的偏移位置为子图的百分比。
get_paths()：获取集合中的路径列表。
set_paths()：设置集合中的路径列表。
set_facecolors()：设置集合元素的填充颜色。
set_edgecolors()：设置集合元素的边缘颜色。
set_linewidths()：设置集合元素的线宽。
set_linestyles()：设置集合元素的线型。
set_segments()：设置集合元素的线段。

参数设置
Edgecolors：可以是color也可以是list of color
default: rcParams["patch.edgecolor"] (default: 'black') 
https://matplotlib.org/stable/api/artist_api.html#module-matplotlib.patches
facecolors：default: rcParams["patch.facecolor"] (default: “C0”)
 
linewidths: default: rcParams["patch.linewidth"] (default: 1.0)
linestyles: str or tuple or list thereof,有效格式包括['solid', 'dashed', 'dashdot', 'dotted', '-', '--', '-.', ':'].
 
Capstyle：线条样式，'butt', 'projecting', 'round'
Joinstyle：用于连接集合中所有路径的线的样式。 'miter', 'round', 'bevel'，
Antialiaseds：线条是否抗锯齿，布尔，默认True
cmap, norm：颜色空间映射和正则化
hatch：路径可以填充的形状，有['/', '', '|', '-', '+', 'x', 'o', 'O', '.', '*'].
Pickradius：当 pickradius <= 0，每当测试点位于由 Collection 中 Path 的控制点形成的多边形之一内部时，Collection.contains会返回True；当pickradius>0时候，会判断测试点是否包含在对应path周围左5，右5的范围内。
Urls：hatch的链接，比如svg
Zorder：绘图顺序，float, default: 1

LineCollection
class matplotlib.collections.LineCollection(segments, *, zorder=2, **kwargs) 
segments：元素为线的list，（line1,line2,line3…）,其中每条线是有m个点组成的line_n = (x0, y0), (x1, y1), ... (xm, ym)
colors：default：“C0”，colors或者list of colors
antialiaseds：default：True，表示是否打开线的抗锯齿
facecolors：设置面颜色时，每条线都被解释为一个区域的边界，隐式关闭从最后一个点到第一个点的路径。对于面的“内部”可以通过PathCollection的 CLOSEPOLY 来指定。
后面的参数可以继承base类，Collection




