import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'A': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2500],
    'B': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],
    'C': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
    "D": [800, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
}

df = pd.DataFrame(data)
print(df.describe())
df.plot.box(title="box plot")
plt.grid(linestyle="--", alpha=0.3)
plt.show()