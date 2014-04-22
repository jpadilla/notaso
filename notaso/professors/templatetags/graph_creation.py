from django import template
from django.conf import settings

from GChartWrapper import Sparkline
from camo import CamoClient

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
    chart.size(450, 262)
    chart.marker('B', 'E6F2FA', 0, 0, 0)
    chart.line(1, 0, 0)
    chart.axes('y')

    if not settings.DEBUG:
        client = CamoClient(settings.CAMO_URL, key=settings.CAMO_KEY)
        url = client.image_url(chart.url)
    else:
        url = chart.url

    return url
