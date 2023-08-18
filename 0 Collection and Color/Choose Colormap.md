# 如何在matplotlib选择适合的色谱  

来源：https://matplotlib.org/stable/tutorials/colors/colormaps.html
### 通过```matplotlib.colormaps```查看内置颜色图  

```
import matplotlib.pyplot as plt
import matplotlib as mpl
cmap = mpl.colormaps['viridis']

data = [[x / 100 for x in range(100)]]

plt.imshow(data, cmap=cmap)
plt.show()
```

### 选择恰当的颜色映射：
选择一个恰当的颜色映射的核心思想是在三维颜色空间中找到适合数据集的表示方式。不同的颜色映射可以将数据的不同值映射为不同的颜色，从而在可视化中呈现出数据的变化。

**选择依据：** 
选择合适的颜色映射取决于多个因素，包括：
- 数据是否表示形状或度量数据（形状数据是指与物体的形状、位置、尺寸等相关的，比如在地图上标记不同城市的位置。对于形状数据，色谱的选择可能会不同，因为颜色并不直接关联物体的形状；度量数据与度量、数量、数值等相关的。例如，绘制一个温度分布图表，或者显示不同地区的人口数量。对于度量数据，色谱的选择可能会着重强调数据的大小、差异和趋势。）
- 对数据集的了解程度（例如，是否有异常值从而与其他值偏离？）
- 是否有关于正在绘制的参数的直观色彩方案
- 是否存在领域内的通用标准

**感知均匀的颜色映射：** 
对于许多应用，选择一种感知上均匀的颜色映射是一个好的选择。感知上均匀的颜色映射指的是数据值的等步变化在颜色空间中被感知为等步变化。研究人员发现，人脑更容易通过亮度参数的变化来感知数据的变化，而不是通过色相的变化。因此，具有在整个颜色映射中单调增加的亮度的颜色映射将更容易被观众理解和解释。
    
**感知均匀颜色映射的例子：** 
在第三方颜色映射部分中，可以找到许多感知上均匀的颜色映射的示例。这些颜色映射的设计可以更好地满足人眼的感知特性，从而使得数据在可视化中更易于理解。

**第三方颜色映射包**（**待探索**）
1. **Aquarel：** 提供了简化的方式来进行灵活的样式和主题设置，用于定制图表的外观。  
2. **CMasher：** 提供了科学领域的颜色映射，用于创建可访问、信息丰富且引人注目的图表。
3. **cmcrameri：** 提供了地球科学领域的感知均匀颜色映射，由Fabio Crameri开发。
4. **cmocean：** 提供了感知均匀的海洋学变量颜色映射，特别适用于海洋学可视化。
5. **cmyt：** 提供了来自yt项目的颜色映射，适用于科学可视化。
6. **Colorcet：** 提供了感知均匀连续颜色映射和感知明显的分类颜色集。
7. **distinctipy：** 提供了任意长度的质感颜色映射，旨在最大程度地保持明显区分。
8. **Farrow&Ball Matplotlib：** 提供了受英国油漆制造商Farrow and Ball启发的颜色调色板。
9. **mplcyberpunk：** 提供了适用于绘图的赛博朋克/霓虹发光效果样式。
10. **TUEplots：** 提供了用于科学出版物中的图表的轻量级Matplotlib样式。
11. **viscm：** 是一个工具，用于分析颜色映射并创建新的颜色映射，帮助你更好地了解和选择合适的颜色映射。

图1：感知均匀的颜色映射（来自Aquarel）
![Alt text](pics/Pasted image 20230818134801.png)
图2：色相、明度（亮度）与饱和度
![Alt text](pics/Pasted image 20230818134938.png)

**不同类别
的颜色映射（colormaps）及应用场景**
1. **Sequential（顺序）** 
这类颜色映射在颜色的明度和饱和度逐渐变化，通常使用单一色调。它们适用于**表示具有顺序的信息**。例如，用于表示温度、海拔高度等逐渐变化的数据。
2. **Diverging（分散）**
这类颜色映射在两种不同颜色的明度和可能的饱和度之间逐渐变化，中间交汇于一个非饱和的颜色。它们适用于在图表中**有一个重要的中间值**，例如地形图中的中间值或数据围绕零偏离的情况。
3. **Cyclic（循环）**
这类颜色映射在两种不同颜色的明度之间逐渐变化，中间在一个非饱和颜色处交汇，并在两端开始/结束于一个非饱和颜色。它们适用于在**值在两端环绕**的情况，例如相位角、风向或一天中的时间。
4. **Qualitative（定性）**
这类颜色映射通常是杂色，用于表示**没有顺序或关系的信息**。它们适用于表示不同类别或类型的数据，其中没有明显的顺序或关联。

**不同类别的颜色映射展示**
1. 顺序图
- 顺序图中，亮度值逐渐单调递增。
- 二进制（二进制颜色映射通常包含只有两种颜色的映射，例如黑色和白色）和其他灰度映射值（灰度颜色映射通常包含一系列不同灰度级别的颜色，从纯黑到纯白）范围可以从0到100，而其他映射的范围一般从30左右开始，具有较小值范围的映射在感知范围上也会相应较小
- 颜色映射中的值函数在不同映射之间有所变化：有些映射在亮度上近似线性，而其他映射则为曲线
![Alt text](pics/Pasted image 20230818151230.png)
![Alt text](pics/Pasted image 20230818151550.png)
![Alt text](pics/Pasted image 20230818152104.png)
2. 分散图
- 在分散型颜色映射中，我们希望亮度值单调递增，直到达到一个最大值，该最大值应接近于100，然后亮度值单调递减
- 在颜色映射的两个相反端点处希望具有近似相等的最小亮度值
![Alt text](pics/Pasted image 20230818153238.png)
3. 循环图
- 在循环型颜色映射中，我们希望从相同的颜色开始和结束，并在中间达到一个对称的中心点。
- 亮度应从开始到中间单调变化，从中间到结束反向变化。
- 它在增加和减少的一侧应对称，并且只在色调上有所不同。
- 在两端和中间，亮度会改变方向，应在亮度空间中进行平滑处理。
![Alt text](pics/Pasted image 20230818153459.png)
 4. 杂色图
 ![Alt text](pics/Pasted image 20230818153708.png)
 5. 其他项
 - 一些颜色映射有特殊用途
 - 'flag': 通常用于标志或国家相关的数据可视化，具有红、白、蓝等颜色。
- 'prism': 用于表示多彩的数据，如光谱或光的折射。
- 'ocean': 用于表示海洋和水域相关的数据，以蓝色为主要颜色。
- 'gist_earth': 用于绘制地形和地球表面数据，融合了绿色、褐色和蓝色。
- 'terrain': 同样用于地形和地球表面数据，也强调了绿色、褐色和蓝色。
-  'gist_rainbow' 和 'rainbow': 常用于展示数据的不同取值，但由于视觉失真，不推荐作为感知映射。
- 'jet': 常用于数据可视化，但同样因为视觉失真，不适合作为感知映射。
- 'turbo': 用于显示深度和视差数据，被设计成在灰度显示时也效果良好。
- 'nipy_spectral' 和 'gist_ncar': 通常用于绘制光谱数据或特定领域的数据。
![Alt text](pics/Pasted image 20230818154315.png)