# HeatMap
以一种直观的方式来观察数据的模式和趋势，两种绘制方法:**matplotlib & seaborn**

内容参考：https://blog.csdn.net/weixin_60737527/article/details/126048311?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522170599894516777224419024%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=170599894516777224419024&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-126048311-null-null.142^v99^pc_search_result_base9&utm_term=%E7%83%AD%E5%9B%BE&spm=1018.2226.3001.4187

## 01 matplotlib绘制热图
#### title设置
- fontdict：设置字体

- loc：'left'、'center'、'right'，表示标题位置，默认为'center'

- rotation：标题逆时针旋转角度，默认为0；x，y：用于进一步控制标题在画布中的位置
#### set_xticks与set_yticks:x轴、y轴坐标设置
- ticks：标签的位置

- labels：标签名

- color：字体颜色

- rotation：字体逆时针旋转角度

- verticalalignment：'center','top','bottom','baseline'，标签垂直对齐

- horizontalalignment：'center','right','left，标签水平对齐

- 如果坐标设置相同，也可以使用 #plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")设置

#### colorbar 标尺
- pad：标尺与图之间距离

- location：'left','right','bottom','top'，标尺的位置。

- orientation：'horizontal','vertical'，标尺方向。

- ticks：列表，如[0,1,2,3..]，显示列表中的刻度。

- extend：'max','min','both'，展示标尺尖角。

- shrink：值为0~1，标尺长度。

- label:标尺标签。

- format：标尺上刻度格式，如’%.2f'表示保留两位小数。

#### tick_params 自定义坐标轴刻度的参数
- axis: 操作的坐标轴，可以是 'x'、'y' 或 'both'。

- which: 应用参数的刻度类型，可以是 'major'（主刻度）、'minor'（次刻度） 或 'both'。

- width、length、color: 刻度的宽度、长度、颜色。

- direction: 刻度的方向，可以是 'in'（朝内）、'out'（朝外） 或 'inout'（内外都有）。

- bottom, top, left, right: 是否启用底部、顶部、左侧或右侧的刻度。

- pad: 刻度与刻度标签之间的距离。

- labelsize: 刻度标签的字体大小。

- labelbottom, labeltop, labelleft, labelright: 是否显示底部、顶部、左侧或右侧的刻度标签。

#### 色块数值显示：text()循环嵌套
- 参数1:x坐标

- 参数2:y坐标

- 参数3:数值标签

- ha:标签水平位置，可以为'left'、'center'、'right'。默认为'center'

- va:标签竖直位置，可以为'top'、 'bottom'、'center'、 'baseline',、center_baseline'。默认为'center'

- color:字体颜色

#### 热图样式：plt.imshow(data,cmap='coolwarm',origin='upper',aspect='auto')

- cmap：热图颜色风格

- origin：热图(0,0)点位置，可以为‘upper'、’lower'。

- aspect：图像长宽比，可以为int或float等数值，auto表示自动匹配

#### grid(which="minor", color="w", linestyle='-', linewidth=3):添加次要刻度的网格线
- which="minor": 指定添加网格线的刻度类型为次要刻度。

- color: 设置网格线的颜色,"w"代表白色。

- linestyle: 设置网格线的线型,'-'表示实线。

- linewidth: 设置网格线的宽度。

#### 也可以定义新的函数，绘制自定风格的热图，具体示例见HeatMap.ipynb文件

## 02 seaborn绘制热图
**sns.heatmap(data=,cmap=,annot=,cbar=,fmt=,linewidth=,linecolor=,xlabelticks=,ylabelticks=,vmax=,vmin=,annot_kws=cbar_kws=,mask=,center= )**

- cmap：热图颜色风格，与matplotlib中cmap相同。

- annot：True,False，是否显示数值注释,默认为False。

- cbar：True,False 是否显示标尺，默认为True。

- linewidth：每个小方格之间的间距。

- linecolor：分割线的颜色。

- xlabelticks,ylabelticks：热图标签。

- vmax,vmin：标尺中最大值与最小值显示值。

- annot_kws：{'color':'  ','size':  ,'family':'  ','style':'  ','weight':  ,......}，单元格数值标签属性。

- cbar_kws:{'orientation':'  ','shrink': '  ' ,'extend:'  ','location':'  ',......}标尺设置。

- mask：可以理解为遮罩。值为Ture,False或0，1等数字的二维数组。若对应位置为False或1，则显示该数据。默认False.示例中将上三角的值设定为1，下三角设定为0，因此只能显示三角形状

- center：将数据设置为均值数据，调整生成图像颜色的整体深浅。

