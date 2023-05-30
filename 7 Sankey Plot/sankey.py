import plotly.graph_objects as go

# data
label = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE"]
source = [0, 0, 1, 1, 0]
target = [2, 3, 4, 5, 4]
value = [8, 2, 2, 8, 4]# data to dict, dict to sankey
link = dict(source = source, target = target, value = value)
node = dict(label = label, pad=50, thickness=5)
data = go.Sankey(link = link, node=node)# plot
fig = go.Figure(data)
fig.show()
