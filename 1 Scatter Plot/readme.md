# **散点图**

## **函数申明**

matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)

## **解析**

**x，y**：输入数据，要求务必长度一致。

**s**：点的大小，默认为rcParams['lines.markersize'] ** 2，也可以是个数组，数组每个参数为对应点的大小。

**c**：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。

**marker**：点的样式，默认小圆圈 'o'。

**cmap**：Colormap，默认 None，标量或者是一个 colormap 的名字，只有 c 是一个浮点数数组的时才使用。如果没有申明就是 image.cmap。 指的是matplotlib.colors.Colormap，相当于多个调色盘的合集

**norm**：Normalize，默认 None，数据亮度在 0-1 之间，只有 c 是一个浮点数的数组的时才使用。

**vmin，vmax**：亮度设置，在 norm 参数存在时会忽略。

**alpha**：透明度设置，0-1 之间，默认 None，即不透明。

**linewidths**：标记点的长度。

**edgecolors**：颜色或颜色序列，默认为 'face'，可选值有 'face', 'none', None。

**plotnonfinite**：布尔值，设置是否使用非限定的 c ( inf, -inf 或 nan) 绘制点。








