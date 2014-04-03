import urllib
import hashlib

from django import template
from django.conf import settings
from GChartWrapper import *
# http://code.google.com/apis/chart/#sparkline  

register = template.Library()
@register.simple_tag
def graph(comments):
    scores = []
    sum_responsibility = 0
    sum_personality = 0
    sum_workload = 0
    sum_difficulty = 0
    count_comment = comments.count()
    print "count: ", count_comment
    for c in comments:
        scores.append(float(c.responsibility-1+c.personality-1 +
                       c.workload-1+c.difficulty-1)*10)
    print scores
    chart = Sparkline(scores)
    chart.color('0077CC')
    chart.size(450,250)
    chart.marker('B', 'E6F2FA',0,0,0)
    chart.line(1,0,0)
    chart.axes('y')
    chart.axes.range(0,10,100,10)
    return chart.img()
    