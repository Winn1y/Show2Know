import matplotlib.pyplot as plt

# 创建数据
size_of_groups = [12, 11, 3, 30]

# 生成饼图
plt.pie(size_of_groups)

# 在中心添加一个圆, 生成环形图
my_circle = plt.Circle((0, 0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(my_circle)

plt.show()