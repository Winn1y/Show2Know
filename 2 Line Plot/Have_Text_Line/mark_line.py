# 需求：绘制一条带方向线和标记文字的曲线图
# ref：https://c.biancheng.net/matplotlib/3d-plot.html
# ref: https://zhuanlan.zhihu.com/p/31302900

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# 找出当前路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 生成2-D数据
X = np.linspace(-np.pi, np.pi, 20, endpoint=True)
Cos, Sin = np.cos(X), np.sin(X)

# 这里显示调用了plt.figure返回一个fig对象, 为了能够后面保存这个fig对象
# 并且设置了fig的大小和每英寸的分辨率
# 注意: resolution = figsize*dpi（因此这里的savefig的分辨率为1200X900）
fig = plt.figure(figsize=(4,3),dpi=300)
ax = plt.gca() # gca： get current axis

# 调用plt.plot函数将两条曲线画在同一个坐标系内，并设置相关的参数
# 设置线条参数：设置颜色，线宽，线形，标记，标记大小，图例标签等等
plt.plot(X, Cos, color='blue', linewidth=1, linestyle='-', marker='>', ms=5, label='cosine')
plt.plot(X, Sin, color='red', linewidth=1, linestyle='--', marker='<', ms=5, label='sine')

# 设置图例（legend）
# plt.legend(loc='auto', frameon=False) # frameon is flag to draw a frame around the legend
# Advanced legend
plt.legend(bbox_to_anchor=(0.02, .95), loc=3,
            borderaxespad=0., frameon=False)

# 设置坐标轴的取值范围（lim）
plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(-1.2, 1.2)

# 设置坐标轴的记号（ticks）
plt.xticks(np.linspace(-np.pi, np.pi, 5, endpoint=True), [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'], )

# 设置坐标轴的标签（label）
plt.xlabel('x_axis')
plt.ylabel('y_axis')

# # 打开grid选项
# plt.grid()

# 移动坐标轴到原点
# 先将上方和右方的spine去掉（color设为none即可）
# 再将x（y）坐标轴设为下方（左方）的spine，并且移动至原点
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 标注（annotate）
# 在x=t处画虚线，并且把(t, y)这个用plt.scatter的方式标记出来
# 在(t, y)处用plt.annotate方法以箭头的方式做标注。
t = 2*np.pi/3

plt.plot([t,t], [0, np.cos(t)], color='blue', linewidth=1, linestyle='--')
plt.scatter([t], [np.cos(t)], 50, color='blue')
plt.annotate(r'$\cos(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
    xy=(t, np.cos(t)), xycoords='data',
    xytext=(-90, -30), textcoords='offset points', fontsize=11,
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

plt.plot([t,t], [0, np.sin(t)], color='red', linewidth=1, linestyle='--')
plt.scatter([t], [np.sin(t)], 50, color='red')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
    xy=(t, np.sin(t)), xycoords='data',
    xytext=(10, 30), textcoords='offset points', fontsize=11,
    arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# 标注（text）
plt.text(-2, 0.8, 'Annotation with pure text', verticalalignment='bottom', horizontalalignment='right',
    color='green', fontsize=8, bbox={'facecolor':'red', 'alpha':0.4, 'pad':2})

# # 将figure保存在path
# fig_name = os.path.join(BASE_DIR, 'figure.jpg')
# fig.savefig(fig_name)
plt.show()