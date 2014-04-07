from django import template
from GChartWrapper import *
# http://code.google.com/apis/chart/#sparkline

from ...comments.models import Comment

register = template.Library()


@register.simple_tag
def graph(professor):
    scores = []
    comments = Comment.objects.filter(
        professor=professor, responsibility__gt=0)
    for c in comments:
        scores.append(float(c.responsibility+c.personality +
                            c.workload+c.difficulty)*5)

    if len(scores) == 0:
        scores.append(0)
    if len(scores) == 1:
        scores.append(scores[0])

    chart = Sparkline(scores, encoding='text')
    chart.color('0077CC')
    chart.size(450, 250)
    chart.marker('B', 'E6F2FA', 0, 0, 0)
    chart.line(1, 0, 0)
    chart.axes('y')
    return chart.img()
