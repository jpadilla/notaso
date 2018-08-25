from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from ..comments.models import Comment
from ..professors.models import Professor
from ..universities.models import University
from .models import Department


class DepartmentView(TemplateView):
    template_name = "department.html"

    def get_context_data(self, **kwargs):
        if "view" not in kwargs:
            kwargs["view"] = self
        uni = get_object_or_404(University, slug=kwargs["slug"])
        department = get_object_or_404(Department, slug=kwargs["department_slug"])
        professors = Professor.objects.filter(
            university=uni, department=department, score__gt=0
        )
        all_professors = Professor.objects.filter(university=uni, department=department)
        comments = (
            Comment.objects.filter(professor__in=professors)
            .exclude(body__exact="")
            .order_by("-created_at", "-id")
        )

        kwargs["university"] = uni
        kwargs["department"] = department
        kwargs["professors"] = all_professors.order_by("first_name")
        kwargs["hi_professors"] = professors.order_by("score").reverse()[:5]
        kwargs["low_professors"] = professors.order_by("score")[:5]
        kwargs["recent_comments"] = comments[:5]
        return kwargs
