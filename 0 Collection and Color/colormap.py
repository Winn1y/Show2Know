'''
    #关于版本 3.7以前版本需选择colormap.md最后三个函数进行注册颜色映射、取消注册、获取指定名称的Colormap对象
    #如何查看matplotlib的版本
'''
import matplotlib
print(matplotlib.__version__)

'''
    # matplotlib.cm模块
    Matplotlib库中的一个子模块，用于处理颜色映射（colormaps）。它提供了一系列预定义的颜色映射对象，可以将数值数据映射到颜色空间，用于可视化数据。
    
    官方链接：https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.get_cmap
    
    本介绍主要包括两个类`class matplotlib.cm.ColormapRegistry(cmaps)`、`class matplotlib.cm.ScalarMappable(norm=None, cmap=None)`及其中可调用的函数。
    
    ## /`class matplotlib.cm.ColormapRegistry(cmaps)`
    提供了类似字典的接口，可以通过名称来访问已注册的颜色映射。它允许用户注册自定义的颜色映射，并提供了一种方便的方式来管理和访问这些颜色映射。
    
    - 使用类字典方式通过名称获取对应的Colormap,这种方式所读取的色谱是副本，对其进行修改并不会影响到全局色谱
    ```python
    import matplotlib as mpl
    cmap = mpl.colormaps['viridis']
    ```

    - 添加colormap到colormaps中：
    ```python
    mpl.colormaps.register(my_colormap)
    ```
    
    ### /`get_cmap(cmap)`
    返回指定的颜色图
    
    **cmap**:取值为字符串、`Colormap`对象、None
    - 字符串，在`mpl.colormaps`中搜索并返回对应的colormap对象
    - `Colormap`直接返回此对象
    - None，返回`rcParams["image.cmap"]`定义的Colormap，默认为`'viridis'`
      
    ### /`register(_cmap_, _*_, _name=None_, _force=False_)`  
    
    注册一个新的色谱,名称可以用作Matplotlib中任何cmap参数的字符串参数

    **cmap**:要注册的matplotlib.colors.Colormap对象，cmap参数是必需的，它应该是一个有效的Colormap对象。可以使用预定义的Colormap对象（如matplotlib.cm.viridis）或自定义的Colormap对象
    
    **name**（可选参数）:字符串格式，如果未提供，则使用`cmap.name`作为名称
    
    **force**:默认False，当尝试覆盖已经注册的名称时，将引发ValueError；设置为Ture,则允许覆盖（谨慎选择True）
    
    ### /`unregister(name)
    
    从注册表中删除色谱
    
    **name**:字符串格式
    
    ⚠️ 
    - 无法删除内置的颜色映射。
    - 如果色谱未注册，不会报错
    - 如果试图取消默认色谱，会报错

    ## /`class matplotlib.cm.ScalarMappable(norm=None, cmap=None)`
    用于将数据值映射到颜色映射（colormap）的范围。
    
    **norm**:设定数据归一化的方式，取值为`Normalize`及其子项、字符串、None
    - `Normalize`及其子项:Normalize、LogNorm、SymLogNorm、PowerNorm
    - 字符串:根据该字符串生成相应的归一化对象。生成的归一化对象会根据数据的范围进行归一化，使数据值在 [0, 1] 的区间内。如"linear"、"power"、"log"
    - None:默认使用colors.Normalize对象作为归一化方式
    
    **cmap**:将归一化数值映射到RGBA颜色，取值为字符串、Colormap对象
    
    ### /`autoscale()`
    根据数据的范围动态调整规范化实例的标量范围，以确保数据在合适的范围内显示。这样可以正确地缩放颜色映射，确保颜色准确地代表数据值。
    
    ### /`autoscale_None()`
    会检查图形对象的限制（如x轴和y轴的限制）是否为None。如果某个限制为None，即未手动设置，则会根据该对象所包含的数据来自动确定该限制的合适取值。
    
    ### /`changed()`
    在标量映射对象发生了改变时进行通知

    ### /`colorbar`
    这里是说colorbar是ScalarMappable 对象的一个属性，用于引用最后一个关联的颜色条。最后这个关联的颜色条可能为 None，表示当前的 ScalarMappable 对象没有与之关联的颜色条。
    
    ### /`get_alpha()`
    获取标量映射对象的透明度参数，返回的是浮点数，且始终为1
    
    ### /`get_array()`
    返回映射到颜色的值的数组（对数组的维度没有要求）
    
    ### /`get_clim()`
    返回映射到颜色映射边界的值，也就是最小值、最大值
    
    ### /`get_cmap()`
    返回所使用的颜色映射colormap实例
    
    ### /`property norm`
    通过property关键字定义的属性norm,可以像访问普通属性一样进行访问,从而获取norm归一化属性
    
    ### /`set_array(A)`
    设置与颜色相关联的值数组

    **A**:数组、None（对数组的维度没有要求）
    
    ### /`set_clim(vmin=None, vmax=None)`
    设置颜色映射的数据范围
    
    **vmin、vmax**:float、None,也可以使用元组（vmin, vmax）
    
    ### /`set_cmap(cmap)`
    设置颜色映射方式，可以为灰（亮）度数据设置颜色映射方式
    
    **cmap**:colormap对象、字符串、None
    
    ### /`set_norm(norm)`
    设置归一化方式
    
    **norm**:Normalize、字符串、None
    
    ⚠️设置可映射对象的规范时，与该规范相关联的颜色条的规范、刻度定位器和标签格式化程序将被重置为默认值
    
    ### /`to_rgba(x, alpha=None, bytes=False, norm=True)`
    返回x对应的规范化rgba数组
    
    **x**:颜色参数，可以是字符串、RGB元组、RGBA元组、十六进制值等
    
    **alpha**:可选参数，用于指定颜色的透明度。如果未提供，将根据x的类型进行自动推断
    
    **bytes**:False（默认值），则获得的rgba数组将在0-1范围内浮动；如果为True，则返回的rgba数组将为0到255范围内的uint8格式
    
    **norm**:False，则不执行输入数据的归一化，并且假设其在范围（0-1）内;Ture，进行归一化到（0-1），默认为Ture
    
    ### /`matplotlib.cm.get_cmap(name=None, lut=None)`[3.7以前版本可用]
    获取指定名称的Colormap对象，3.7及以后版本改用matplotlib.colormaps[name]或matplotlb.colormaps.get_cmap（obj）
    
    ### /`matplotlib.cm.register_cmap(name=None, cmap=None, *, override_builtin=False)`[3.7以前版本可用]
    注册新的颜色映射，3.7及以后版本使用`matplotlib.colormaps.register(name)`替代
    
    ### /`matplotlib.cm.unregister_cmap(name)`[3.7以前版本可用]
    取消注册颜色映射，3.7及以后版本使用`matplotlib.colormaps.unregister(name)`替代
'''
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np
import matplotlib.pyplot as plt

'''#Demo1:get_cmap函数所获取内容为colormap对象，为matplotlib中的一种数据类型'''
cmap = cm.get_cmap('viridis')
print(cmap) # <matplotlib.colors.ListedColormap object at 0x7fbb60a6ec40>

'''#Demo2:取消注册颜色映射'''
cm.unregister_cmap('my_cmap01')

'''#Demo3: 创建自定义离散颜色映射'''
cmap_data = np.random.rand(256, 3)  # 生成256个随机颜色
my_cmap = colors.ListedColormap(cmap_data, name='my_cmap')
cm.register_cmap(cmap=my_cmap)
x = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * x)
plt.scatter(x, y, c=x, cmap='my_cmap')
plt.colorbar()
plt.show()

'''#Demo4: 创建自定义连续渐变颜色映射'''
colors_list = ['orange', 'blue']
mycmap = colors.LinearSegmentedColormap.from_list('my_cmap03', colors_list)
cm.register_cmap(cmap=mycmap)
x = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * x)
plt.scatter(x, y, c=x, cmap='my_cmap03')
plt.colorbar()
plt.show()

'''#Demo5: ScalarMappable使用'''
data = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
scalar_mappable = cm.ScalarMappable(norm=colors.Normalize(), cmap='viridis')
scalar_mappable.set_array(normalized_data)
my_norm = colors.PowerNorm(gamma=0.5)
scalar_mappable.set_norm(my_norm)
alpha = scalar_mappable.get_alpha()
array = scalar_mappable.get_array()
cmap = scalar_mappable.get_cmap()
scalar_mappable.set_clim(vmin=0.5, vmax=2)
scalar_mappable.autoscale()
clim = scalar_mappable.get_clim()
x = np.linspace(0, 1, 100)
y = np.sin(2 * np.pi * x)
plt.scatter(x, y, c=x, cmap='viridis',norm=my_norm)
plt.colorbar(scalar_mappable)
plt.show()

'''#Demo6: to_rgba函数的使用'''
values = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
colors = scalar_mappable.to_rgba(values)
for value, color in zip(values, colors):
    print(f"Value: {value}, Color: {color}")
x = np.arange(len(values))
y = np.zeros_like(x)
plt.scatter(x, y, color=colors)
plt.show()

'''#Demo7: 灰度数据的颜色映射'''
image = np.random.rand(100, 100)
sm = plt.cm.ScalarMappable()
sm.set_cmap('viridis')
plt.imshow(image, cmap=sm.get_cmap())
plt.colorbar()
plt.show()

