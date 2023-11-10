"""
    近期论文需要对特征降维后可视化，一般采用t-sne进行降维并可视化
    一般情况下 可视化后的效果应该分类明显，类别应该呈现”一坨“堆叠在一起
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
from glob import glob
import os
from tqdm import tqdm
import random

"""
    
"""

cate = [1,2,3]

cate1 = [[random.random() // 2  for _ in range(768)] for _ in range(200)]
cate1_label = [1 for _ in range(200)]

cate2 = [[random.random() * 10  for _ in range(768)] for _ in range(200)]
cate2_label = [2 for _ in range(200)]

cate3 = [[random.random() * 3 + random.random()  for _ in range(768)] for _ in range(200)]
cate3_label = [3 for _ in range(200)]

x = np.concatenate([cate1, cate2, cate3], dtype=np.float32)
y = np.concatenate([cate1_label, cate2_label, cate3_label], dtype=np.float32)

print(x.shape)  # (600, 768)
print(y.shape)  # (600,)


tsne = manifold.TSNE(n_components=2, perplexity=50, init='pca', random_state=42).fit_transform(x)
x_min, x_max = tsne.min(0), tsne.max(0)
tsne_norm = (tsne - x_min) / (x_max - x_min)

# 无正则化
plt.figure(figsize=(8, 8))
for i in cate:
    plt.scatter(tsne[y == i][:, 0], tsne[y == i][:, 1], 8, label=i)
plt.legend(loc='upper left')
plt.show()

# 正则化
plt.figure(figsize=(8, 8))
for i in cate:
    plt.scatter(tsne_norm[y == i][:, 0], tsne_norm[y == i][:, 1], 8, label=i)
plt.legend(loc='upper left')
plt.show()