import os
import numpy as np
try:
    import pandas as pd
    USE_PD = True
except Exception:
    USE_PD = False
import matplotlib.pyplot as plt
try:
    import seaborn as sns
    USE_SNS = True
except Exception:
    USE_SNS = False
np.random.seed(42)
methods = ['disco', 'champ', 'magicpose']
n = 30
ssim = {
    'disco': np.clip(np.random.normal(0.7, 0.06, n), 0, 1),
    'champ': np.clip(np.random.normal(0.72, 0.05, n), 0, 1),
    'magicpose': np.clip(np.random.normal(0.78, 0.04, n), 0, 1)
}
psnr = {
    'disco': np.random.normal(15, 2.2, n),
    'champ': np.random.normal(16, 2.0, n),
    'magicpose': np.random.normal(18, 1.8, n)
}
os.makedirs('output', exist_ok=True)
if USE_SNS and USE_PD:
    rows = []
    for m in methods:
        for v in ssim[m]:
            rows.append({'method': m, 'metric': 'ssim', 'value': float(v)})
        for v in psnr[m]:
            rows.append({'method': m, 'metric': 'psnr', 'value': float(v)})
    df = pd.DataFrame(rows)
    sns.set(style="whitegrid")
    palette = sns.color_palette("Set2")
    df_ssim = df[df['metric'] == 'ssim']
    plt.figure(figsize=(8, 5))
    sns.violinplot(data=df_ssim, x='method', y='value', palette=palette, inner='quartile', cut=0)
    sns.boxplot(data=df_ssim, x='method', y='value', width=0.15, boxprops={'facecolor': 'none'}, showcaps=False, whiskerprops={'linewidth': 1}, medianprops={'linewidth': 2})
    sns.swarmplot(data=df_ssim, x='method', y='value', color='k', size=2, alpha=0.6)
    plt.title('Violin Plot - SSIM')
    plt.grid(linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/violin_ssim.png')
    plt.close()
    plt.figure(figsize=(8, 5))
    sns.violinplot(data=df, x='method', y='value', hue='metric', split=True, palette=palette, inner='quartile', cut=0)
    plt.title('Split Violin Plot - SSIM vs PSNR')
    plt.grid(linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/violin_split.png')
    plt.close()
else:
    order = methods
    data = [ssim[m] for m in order]
    plt.figure(figsize=(8, 5))
    plt.violinplot(data, showmeans=True, showmedians=True, showextrema=True)
    plt.xticks(np.arange(1, len(order) + 1), order)
    plt.title('Violin Plot - SSIM (matplotlib)')
    plt.grid(linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('output/violin_ssim.png')
    plt.close()
