# 误差线
来源：《PythonDataScienceHandbook[1]》(Python 数据科学手册[2])第四章Matplotlib介绍部分

出发点：公认值大概是 71±2.5(km/s) / Mpc，而测量值是 74±5(km/s) / Mpc。测量数据与公认值是否一致？这个问题可以从定量的角度进行回答。

## 基本误差线
基本误差线（errorbar）可以通过 Matplotlib 中errorbar函数来创建：
```
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='.k');
```
## matplotlib.pyplot.errorbar
来源 https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html
matplotlib.pyplot.errorbar(x, y, yerr=None, xerr=None, fmt='', ecolor=None, elinewidth=None, capsize=None, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None, *, data=None, **kwargs)
**参数解释**
**x,y**:数据位置
**yerr**:纵向误差条的大小,>=0。可选值：「标量」所有数据点的对称 +/- 值）；「shape(N,)」每个数据点的对称+/-值；「shape(2,N)」每个条形的单独 - 和 + 值。第一行包含较低的错误，第二行包含较高的错误；「None」无错误值
**xerr**:横向误差条的大小,>=0,类似yerr.
**fmt**:数据点的格式字符串。例如，'o' 表示圆圈，'-' 表示实线，'.k' 表示黑色的点。None 表示绘制没有任何数据标记的误差线
**ecolor**:误差条的颜色。可选值：颜色名称'red'；RGB元组(1, 0, 0)。None 表示使用连接标记的线条的颜色
**elinewidth**:误差线的线宽.float。None表示使用当前样式的线宽
**capsize**: 误差条两端的横线的大小。float
**barsabove**: 误差条是否在数据点上方。bool值，默认False
**lolims, uplims, xlolims, xuplims**: 是否显示下限/上限（指定为True时，误差条相应方向上将以箭头表示）。
**errorevery**: int.控制显示误差条的点的密度。例如，errorevery=2 表示每两个点显示一个误差条。
**capthick**: 误差条两端横线的线宽。
**data**:可索引对象，可选
**kwargs**:函数可以接受额外的关键字参数，这些参数会被打包成一个字典（dictionary），可以在函数体内部使用。

## 连续误差
有时候可能需要显示连续变量的误差。虽然 Matplotlib 没有内置的简便方法可以解决这个问题，但是通过 plt.plot 与 plt.fill_between 来解决也不是很难。我们将用 Scikit-Learn 程序库 API 里面一个简单的高斯过程回归方法（Gaussian process regression，GPR）来演示。这是用一种非常灵活的非参数方程（nonparametric function）对带有不确定性的连续测量值进行拟合的方法。这里不会详细介绍高斯过程回归方法的具体内容，而是将注意力放在数据可视化上面：
```
from sklearn.gaussian_process import GaussianProcessRegressor

# 定义模型和一些符合模型的点
model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)

# 计算高斯过程回归，使其符合 fit 数据点
gp = GaussianProcessRegressor()
gp.fit(xdata[:, np.newaxis], ydata)

xfit = np.linspace(0, 10, 1000)
yfit, std = gp.predict(xfit[:, np.newaxis], return_std=True)
dyfit = 2 * std  # 两倍sigma ~ 95% 确定区域
```
以上代码可获得xfit、yfit和dyfit。使用plt.fill_between函数在误差限区域内填充一道浅色的误差带来展示连续误差
```
# 可视化结果
plt.plot(xdata, ydata, 'or')
plt.plot(xfit, yfit, '-', color='gray')

plt.fill_between(xfit, yfit - dyfit, yfit + dyfit,
                 color='gray', alpha=0.2)
plt.xlim(0, 10);
```
调用fill_between函数：我们传递了的参数包括 x 值，y 值的低限，然后是 y 值的高限，结果是图表中介于低限和高限之间的区域会被填充。
上图为我们提供了一个非常直观的高斯过程回归展示：在观测点的附近，模型会被限制在一个很小的区域内，反映了这些数据的误差比较小。在远离观测点的区域，模型开始发散，反映了这时的数据误差比较大。