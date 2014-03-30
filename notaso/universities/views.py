from django.db.models import Count
from django.shortcuts import render, get_object_or_404

from ..departments.models import Department
from ..professors.models import Professor
from ..comments.models import Comment

from .models import University


def universities_view(request):
    universities = University.objects.all().annotate(
        Count('professor')).order_by('-professor__count', '-emblem')

    data = {
        'universities': universities
    }

    return render(request, "universities.html", data)


def specific_university_view(request, slug):
    university = get_object_or_404(University, slug=slug)

    professors = Professor.objects.filter(
        university=university).select_related('university')

    comments = Comment.objects.filter(
        professor__in=professors).select_related(
        'created_by').exclude(body__exact='')

    data = {
        'specified_university': university,
        'departments': Department.objects.all(),
        'hi_professors': professors.order_by('-score')[:5],
        'grade': university.get_grade(),
        'low_professors': professors.order_by('score')[:5],
        'recent_comments': comments.order_by('-created_at')[:5]
    }

    return render(request, "university.html", data)
