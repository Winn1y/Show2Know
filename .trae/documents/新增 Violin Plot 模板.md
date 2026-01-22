## 推荐模板：Violin Plot（小提琴图）
- 用途：在已有 Box Plot 的基础上，更直观展示分布形状（峰/厚尾/多峰），对比不同方法或分组的整体分布。
- 适配度：项目已使用 matplotlib/seaborn，直接用 seaborn.violinplot 实现，风格与现有文件保持一致。
- 参考现有风格：见 [box_plot.py](file:///j:/清华资料合集/【核心发展】学业基本资料/研一下课程/数据可视化/作业/Show2Know/10%20Box%20Plot/box_plot.py) 与 [scatter.py](file:///j:/清华资料合集/【核心发展】学业基本资料/研一下课程/数据可视化/作业/Show2Know/1%20Scatter%20Plot/scatter.py)。

## 文件结构与命名
- 新增目录：19 Violin Plot/
- 文件：
  - violin.py（可运行示例，保存 PNG 到 output/）
  - ViolinPlot.md（简短用法说明与参数解释）
  - output/（示例输出图）

## 实现要点（脚本内容）
- 依赖：matplotlib、pandas、seaborn（与现有仓库一致）。
- 数据形态：长表格式（columns：method, metric, value），支持从宽表 melt 到长表。
- 基本绘制：
  - sns.set(style="whitegrid")，配色使用 sns.color_palette("Set2")。
  - sns.violinplot(data=df, x="method", y="value", hue="metric", split=True 或分面方式)。
  - inner="quartile" 显示四分位；可选显示均值点。
- 增强叠加（可选开关）：
  - sns.boxplot(width=0.15, dodge=True) 叠加精简箱线，突出中位数与 IQR。
  - sns.swarmplot(size=2, alpha=0.6) 叠加离散点，展示个体分布。
- 导出：plt.tight_layout(); plt.savefig("output/violin_demo.png"); plt.show()。

## 示例数据与流程
- 从现有 exp_box_plot.py 的数据结构出发，构造 DataFrame 宽表，并通过 pandas.melt 转为长表：
  - 宽表列名示例：disco_ssim, champ_ssim, ...；行是样本。
  - melt 后得到 method（来源列前缀）、metric（如 ssim/psnr）、value。
- 参数化：
  - 允许用户选择 x（method）、hue（metric）、是否 split、是否叠加 box/swarm、调色板、透明度等。

## 与现有代码的风格一致性
- 保持“脚本即示例”的简单入口，类似 [box_plot.py](file:///j:/清华资料合集/【核心发展】学业基本资料/研一下课程/数据可视化/作业/Show2Know/10%20Box%20Plot/box_plot.py)。
- 输出目录与命名统一为 output/xxx.png，便于查阅与版本化。

## 验收标准
- 运行 violin.py 成功生成 1–2 张示例图：
  - 单 metric 的分组小提琴图
  - 多 metric 的 split 小提琴图（或 Facet 分面）
- 图例清晰、颜色一致、标题/轴标注完备、栅格线风格统一。

## 备选模板（如需改选）
- Hexbin Plot（二维密度）：适合点密集的散点数据，补全 2DHist 的蜂窝可视化。
- Dumbbell Plot（哑铃图）：突出两时点或两方案的差异变化。
- Radar Chart（雷达图）：对比多维特征，但需谨慎标尺与排序。

## 下一步
- 我将按以上方案新增 19 Violin Plot 目录与示例脚本、文档，并确保与现有风格/依赖一致；如确认该模板优先级最高，后续可再补充 Hexbin/Dumbbell 作为扩展。