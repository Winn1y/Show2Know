# matplotlib / pyecharts

import pyecharts.options as opts
from pyecharts.charts import Line
x=['星期一','星期二','星期三','星期四','星期五','星期七','星期日']
y=[100,200,300,400,500,400,300]

line=(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=x)
    .add_yaxis(
        series_name="基本折线图",
        y_axis=y,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
)
line.render()
