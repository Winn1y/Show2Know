import matplotlib.pyplot as plt
import squarify
import pandas as pd

# 创建数据
df = pd.DataFrame({'nb_people': [8, 3, 4, 2], 'group': ["group A", "group B", "group C", "group D"]})

# 绘图显示
squarify.plot(sizes=df['nb_people'], label=df['group'], alpha=.8 )
plt.axis('off')
plt.show()