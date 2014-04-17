from django.db.models import Count
from django.views.generic import TemplateView, DetailView

from ..departments.models import Department
from ..professors.models import Professor
from ..comments.models import Comment

from .models import University


class UniversitiesView(TemplateView):
    template_name = 'universities.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        kwargs['universities'] = University.objects.all().annotate(
            Count('professor')).order_by('-professor__count', '-emblem')
        return kwargs


class UniversityView(DetailView):
    model = University
    template_name = 'university.html'

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self

        professors = Professor.objects.filter(
            university=self.object,
            score__gt=0).select_related('university')
        comments = Comment.objects.filter(
            professor__in=professors).select_related(
                'created_by').exclude(
                    body__exact='').order_by('-created_at', '-id')

        kwargs['specified_university'] = self.object
        kwargs['grade'] = self.object.get_grade()
        kwargs['departments'] = Department.objects.all()
        kwargs['hi_professors'] = professors.order_by('-score')[:5]
        kwargs['low_professors'] = professors.order_by('score')[:5]
        kwargs['recent_comments'] = comments.order_by('-created_at')[:5]
        return kwargs
