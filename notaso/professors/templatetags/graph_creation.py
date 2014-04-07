from django import template
from GChartWrapper import *
# http://code.google.com/apis/chart/#sparkline

register = template.Library()


@register.simple_tag
def graph(comments):
    scores = []
    for c in comments:
        scores.append(float(c.responsibility-1+c.personality-1 +
                            c.workload-1+c.difficulty-1)*10)
    chart = Sparkline(scores)
    chart.color('0077CC')
    chart.size(450, 250)
    chart.marker('B', 'E6F2FA', 0, 0, 0)
    chart.line(1, 0, 0)
    chart.axes('y')
    chart.axes.range(0, 10, 100, 10)
    return chart.img()
