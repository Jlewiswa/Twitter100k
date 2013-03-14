from pygooglechart import SimpleLineChart,Axis

def getLineGraph(data,line1color,line2color):
    # Set the vertical range based on data values
    tweets = [d[0] for d in data]
    retweets = [d[1] for d in data]
    ratio = [str(int(d[1]/d[0]*100))+'%' for d in data]
    hours = [d[2] for d in data]
    mx = max(tweets)
    mn = min(retweets)
    buffer = (mx - mn)/100 # average retweets have consitently been less
    min_y = mn - buffer
    max_y = mx + buffer

    # Chart size of 750x400 pixels and specifying the range for the Y axis
    chart = SimpleLineChart(750, 400, y_range=[min_y, max_y])
    chart.set_legend(['Tweets','Retweets'])
    chart.set_legend_position('t')
    # Add the chart data
    chart.add_data(tweets)
    chart.add_data(retweets)
    # Set the line colour to blue
    chart.set_colours([line1color,line2color])

    # Set the horizontal dotted lines
    chart.set_grid(0, 25, 5, 5)

    #set left axis to values range
    left_axis = range(min_y, max_y, (max_y-min_y)/10)
    chart.set_axis_labels(Axis.BOTTOM, hours)
    chart.set_axis_labels(Axis.BOTTOM, ratio)
    chart.set_axis_labels(Axis.LEFT, left_axis)
    return chart.get_url()

