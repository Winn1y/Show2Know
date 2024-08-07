import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Category': ['2017', '2020', '2023', '2024'],
    'Year': [1, 5, 46, 69],
})

with plt.xkcd():
    fig, ax = plt.subplots(figsize=(6.5, 4.4), dpi=100)
    df.plot.bar(x='Category', y='Year', color=["#0972B5"], edgecolor="black", rot=10, ax=ax)
    ax.set_xticklabels(df['Category'])
    ax.set_ylim((0, 75))
    ax.legend(frameon=True)
    ax.text(0.8, -0.22, 'Visualization by DataCharm', transform=ax.transAxes,
            ha='center', va='center', fontsize=10, color='black')
    plt.show()
