from django import template

from ...comments.models import Comment


register = template.Library()


@register.simple_tag
def graph_data(professor):
    scores = []
    comments = Comment.objects.filter(
        professor=professor,
        responsibility__gt=0
    )

    for c in comments:
        scores.append(c.score)

    if len(scores) == 0:
        scores.append(0)

    if len(scores) == 1:
        scores.append(scores[0])

    return ','.join(map(str, scores))
