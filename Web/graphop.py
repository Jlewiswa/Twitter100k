from pygooglechart import StackedVerticalBarChart,Axis

def getGraph(data,barcolor):
    last = len(data)-1
    spread = data[0][1] - data[last][1]
    buffer = spread/100
    min = 0
    max = 100
    if data[last][1] > 10:
        min = data[last][1] - buffer
    if data[0][1] > 10:
        max = data[0][1] + buffer
    chart = StackedVerticalBarChart(750, 400,y_range=(min,max))

    chart.set_bar_width(65)
    chart.set_colours([barcolor])
    chart.add_data([d[1] for d in data])
    chart.set_axis_labels(Axis.BOTTOM, [d[0] for d in data])
    chart.set_axis_labels(Axis.BOTTOM, [d[1] for d in data])
    return chart.get_url()