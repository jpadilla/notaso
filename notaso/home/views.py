from django.views.generic import TemplateView

from ..professors.models import Professor
from ..universities.models import University
from ..comments.models import Comment


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self

        universities = University.objects.all()
        universities = list(universities)
        universities.sort(key=lambda x: x.get_grade())

        professors = Professor.objects.filter(score__gt=0).order_by('-score')

        comments = Comment.objects.all().exclude(
            body__exact='').order_by('-created_at', '-id')

        kwargs['professors'] = professors[:5]
        kwargs['universities'] = universities[:5]
        kwargs['recent_comments'] = comments[:5]
        kwargs['navbarSearchShow'] = True
        return kwargs
