import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
#绘制50条线
N = 50
x = np.arange(N)
ys = [x + i for i in x]  # Many sets of y to plot vs. x
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

line_segments = LineCollection(segs,
                               array=x,
                               linewidths=(0.5, 1, 1.5, 2,4,6),#设置线条宽度
                               colors=colors,#设置颜色
                               linestyles='dashed',#设置线条为短虚线
                               # antialiaseds=False,#抗锯齿关闭
                               )
ax.add_collection(line_segments)
# 这段决定colorbar
# axcb = fig.colorbar(line_segments)
# axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)  # This allows interactive changing of the colormap.
plt.show()