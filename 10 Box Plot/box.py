import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100]

df = pd.DataFrame(data)
df.plot.box(title="hua tu")
plt.grid(linestyle="--", alpha=0.3)
plt.show()