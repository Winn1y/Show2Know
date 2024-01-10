import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import make_interp_spline, BSpline
import statsmodels.api as sm
lowess = sm.nonparametric.lowess

# 生成示例散点数据（使用正态分布和均匀分布）
np.random.seed(20)
x1 = np.sort(10 * np.random.randn(100))  # 正态分布
x2 = np.sort(10 * np.random.rand(40))   # 均匀分布
x = np.concatenate([x1, x2])

# 添加更多噪声
y = 2 * x + 1 + np.sin(x) + 5 * np.random.randn(len(x))

# 对 x 进行排序
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]

# 绘制散点图
plt.scatter(x, y, label='Basic Data')

# 局部加权散点拟合
# lowess函数会返回两列numpy数据，第一列是原始数据拟合不平滑的结果，第二列是平滑一下后的数据
# 其中frac越大，加权散点拟合的效果越平滑
# missing =  (‘none’, ‘drop’, and ‘raise’) 'none'不进行缺失值检查，'drop'丢弃含有缺失值的样本(默认), 'raise'有缺失值会报错
# yest0 = lowess(y_sorted,x_sorted)
yest0 = lowess(y_sorted, x_sorted, frac=1./3.)[:,0]
yest = lowess(y_sorted, x_sorted, frac=1./3.)[:,1]
# loess_fit = make_interp_spline(x_sorted, y_sorted, k=3)
# loess_curve = loess_fit(x_sorted)
plt.plot(x_sorted, yest0, label='Locally weighted scatter fitting(no smoothy)', color='yellow')
plt.plot(x_sorted, yest, label='Locally weighted scatter fitting(smoothy)', color='green')

# 线性拟合
# 1表示这是一条拟合的线性直线
linear_fit = np.polyfit(x_sorted, y_sorted, 1)
linear_curve = np.poly1d(linear_fit)
plt.plot(x_sorted, linear_curve(x_sorted), label='Linear Fitting', color='orange')

# 多项式拟合曲线
#其中10表示多项式的次数为10次
poly_fit = np.polyfit(x_sorted, y_sorted, 10)
poly_curve = np.poly1d(poly_fit)
x_poly = np.linspace(min(x_sorted), max(x_sorted), 100)
plt.plot(x_poly, poly_curve(x_poly), label='polynomial fitting Quadratic', color='purple')

# 计算趋势带（可根据需要调整标准差倍数）
std_dev = np.std(y_sorted)
upper_band = yest + 2 * std_dev
lower_band = yest - 2 * std_dev

# 绘制趋势带
plt.fill_between(x_sorted, upper_band, lower_band, alpha=0.2, color='green', label='trend band')

plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Fitting curves and locally weighted scatter fitting')
plt.show()
