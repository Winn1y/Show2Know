import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

"""
    seaborn.heatmap(data, vmin=None, vmax=None, 
                    cmap=None, center=None, robust=False, 
                    annot=None, fmt='.2g', annot_kws=None, 
                    linewidths=0, linecolor='white', cbar=True, 
                    cbar_kws=None, cbar_ax=None, square=False, 
                    xticklabels='auto', yticklabels='auto', 
                    mask=None, ax=None, **kwargs)
"""

uniform_data = np.random.rand(10, 12)
f, ax = plt.subplots(figsize=(9, 6))

ax = sns.heatmap(uniform_data)
plt.show()