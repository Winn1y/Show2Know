# Sankey

### Sankey is?
桑基图（Sankey Diagram）是一种特定类型的流程图，也叫桑基能量平衡图，用于描述一组值到另一组值的流向。

### When Sankey?
1. 综述领域论文时候，系列论文随类别变化，其从属的节点发生变化，这样可以拆出主要的类别和主要的研究方法/框架。
2. 用户行为分析时候，直观的展现用户旅程，发现用户的兴趣点和流失点，发现被用户忽略的产品价值点。
3. 还需要补充...
### How Sankey?

plotly go.Sankey 如何实现桑基图，主要依靠node和link的定义。
1. node绘制：流量改变的节点
   1. pad：节点之间的间距；
   2. thickness：节点本身的厚度；
   3. line：可以定义从node发出的线条的颜色；
   4. label：每个node对应的名称。
2. link绘制：主要由source、target、value、label四个参数来确定link。
   1. source：每一个link的出发点的对应的node中的label的索引（从0开始）；
   2. target：每一个link的终止点对应的node中的label的索引（从0开始）；
   3. value：每一个link对应的流量的数值大小；
   4. label：每一个link对应的名称。
