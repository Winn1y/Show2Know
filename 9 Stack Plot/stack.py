import matplotlib.pyplot as plt

# 创建数据
x = range(1, 6)
y1 = [1, 4, 6, 8, 9]
y2 = [2, 2, 7, 10, 12]
y3 = [2, 8, 5, 10, 6]

# 生成图表
plt.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'])
plt.legend(loc='upper left')
plt.show()