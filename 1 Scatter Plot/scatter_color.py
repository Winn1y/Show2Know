import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors  # 注意！为了调整“色盘”，需要导入colors

rng = np.random.RandomState(0)
x = rng.randn(50)
y = rng.randn(50)
color = rng.rand(50)
sizes = 700 * rng.rand(50)

changecolor = colors.Normalize(vmin=0.4, vmax=0.8)

plt.scatter(x, y, c=color, s=sizes, alpha=0.3, cmap='viridis',norm=changecolor)

plt.colorbar()
plt.show()