# **散点图**

## 函数说明
matplotlib.pyplot.scatter(  x, y, s=None, c=None, 
                            marker=None, cmap=None, 
                            norm=None, vmin=None, 
                            vmax=None, alpha=None, 
                            linewidths=None, verts=<deprecated parameter>, 
                            edgecolors=None, *, plotnonfinite=False, data=None, **kwargs )

## 官方链接
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib-pyplot-scatter

## 参数说明

/ x, y：         
点的位置，x, y支持多维数组，但是x, y的维度必须一致，多维数组会被展平（flatten）为一维数组。
/ s： （可选参数）            
标记的面积，也支持多维数据。默认值为rcParams['lines.markersize'] ** 2。
/ c： （可选参数）           
标记的颜色。支持颜色数组列表或单一颜色。
注意点：
    1. 输入的值将会使用cmap和norm将其映射到颜色条
    2. 支持的二维数组输入，行是RGB或者RGBA
    3. 支持单一的颜色十六进制编码
    4. 支持跟输入维度一样长的颜色编码
/marker：        
点的样式。取值参考matplotlib.markers。默认值为rcParams["scatter.marker"] ('o')。
/cmap：          
色彩映射。已注册的色彩映射名称或Colormap实例。默认值为rcParams["image.cmap"] ('viridis')。
注意点：cmap只能在c参数为浮点数数组时才能使用。
/norm： （可选参数）          
Normalize，默认值为None。如果c参数为浮点数数组，norm参数在[0,1]范围内缩放颜色数据，c构造与cmap的颜色映射。如果为None，默认的colors.Normalize。
注意点：
    1. 如果c为RGB/RGBA类型的二维数组输入，这个值会无效
    2. 支持的norm类型有："linear", "log", "symlog", "logit"
/vmin, vmax： （可选参数） 
颜色值的映射范围。
注意点：
    如果c为RGB/RGBA类型的二维数组输入，这个值会无效。
/alpha：         
浮点数。取值范围为[0,1]，0为透明，1为不透明。默认值为None。
/linewidths：    
标记边缘线宽。浮点数或类数组结构。默认值为rcParams["lines.linewidth"] (1.5)。
默认的边缘颜色为‘face’颜色，可支持修改。
/edgecolors：    
标记边缘颜色，支持直接输入一个颜色序列
取值为{'face', 'none', None}、颜色、颜色序列。默认值为rcParams["scatter.edgecolors"] ('face')。
                 'face'：标记边缘颜色与标记颜色相同
                 'none'：没有边线。
/plotnonfinite：
布尔值，是否绘制非实数内容点，例如inf、nan等
/data：
支持数据批量输入，以以下的形式
x, y, s, linewidths, edgecolors, c, facecolor, facecolors, color 

