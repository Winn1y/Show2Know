import matplotlib.pyplot as plt
import numpy as np

# 数据示例
x = [1, 2, 3, 4, 5, 6]  # x轴数据

# y 数据格式：每个点包含最小值、均值和最大值
data_sets = [
    [[45, 48, 51], [38, 40, 43], [55, 58, 60], [41, 44, 47], [40, 42, 45], [35, 37, 40]],
    [[25, 30, 35], [28, 32, 36], [30, 34, 38], [33, 36, 39], [35, 38, 42], [38, 40, 43]],
    [[55, 60, 65], [58, 62, 66], [60, 64, 68], [63, 66, 69], [65, 68, 72], [68, 70, 73]],
    [[15, 20, 25], [18, 22, 26], [20, 24, 28], [23, 26, 30], [25, 28, 32], [28, 30, 33]],
    [[65, 70, 75], [68, 72, 76], [70, 74, 78], [73, 76, 80], [75, 78, 82], [78, 80, 85]],
    [[5, 10, 15], [8, 12, 16], [10, 14, 18], [13, 16, 20], [15, 18, 22], [18, 20, 24]]
]

# 可指定折线的颜色（十六进制）
colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd', '#ff7f0e', '#8c564b']

# 绘制折线图并指定颜色和点样式
for i, data in enumerate(data_sets):
    means = [y[1] for y in data]
    mins = [y[0] for y in data]
    maxs = [y[2] for y in data]
    plt.plot(x, means, label=f'Line {i+1}', color=colors[i], marker='o')  # 仅绘制均值
    plt.fill_between(x, mins, maxs, color=colors[i], alpha=0.2)  # 填充区域

# 设置y轴的范围
plt.ylim(0, 100)

# 添加标题和标签
plt.title('Multi Line Chart with Fill')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图表
plt.legend()

# 保存图像
plt.savefig('multi_line_chart_with_fill.png')

# 显示图表
plt.show()
