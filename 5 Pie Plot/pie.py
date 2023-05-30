import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆
label = ['第一', '第二', '第三']  # 定义饼图的标签，标签是列表
explode = [0.01, 0.2, 0.01]  # 设定各项距离圆心n个半径
# plt.pie(values[-1,3:6],explode=explode,labels=label,autopct='%1.1f%%')#绘制饼图

values = [4, 7, 9]
plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
plt.title('2018年饼图')
plt.savefig('./2018年饼图')
plt.show()
