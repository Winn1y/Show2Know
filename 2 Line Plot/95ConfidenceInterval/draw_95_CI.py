import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.stats as st
matplotlib.rcParams.update({'font.size': 12})

# 准备数据
data_points = 10
GroundTrue = [10, 25, 77, 197, 12, 44, 67, 84, 11,23]

Sigma = np.ones(data_points) * 80
data = np.random.normal(loc=GroundTrue, scale=Sigma, size=(100, data_points))
predicted_expect = np.mean(data, 0)

# 计算最大最小置信区间
low_CI_bound, high_CI_bound = st.t.interval(0.95, data_points - 1,
                                            loc=np.mean(data, 0),
                                            scale=st.sem(data))

# plot confidence interval
x = np.linspace(0, data_points - 1, num=data_points)
plt.plot(predicted_expect, linewidth=3., label='estimated value')
plt.plot(GroundTrue, color='r', label='grand truth')
plt.fill_between(x, low_CI_bound, high_CI_bound, alpha=0.5,
                label='confidence interval')
plt.legend()
plt.title('Confidence interval')
plt.show()
