from django.db.models import Count
from django.shortcuts import render_to_response, get_object_or_404

from departments.models import Department
from professors.models import Professor
from comments.models import Comment

from .models import University


def universities_view(request):
    universities = University.objects.all().annotate(
        Count('professor')).order_by('-professor__count')

    data = {
        'universities': universities
    }

    return render_to_response("universities.html", data)


def specific_university_view(request, slug):
    university = get_object_or_404(University, slug=slug)
    data = {
        'specified_university': university,
        'departments': Department.objects.all(),
        'hi_professors': Professor.objects.filter(
            university=university).order_by('-score')[:5],
        'grade': university.get_grade(),
        'low_professors': Professor.objects.filter(
            university=university).order_by('score')[:5],
        'recent_comments': Comment.objects.filter(
            professor__in=Professor.objects.filter(
                university=university)).exclude(
        body__exact='').order_by('-created_at')[:5]
    }
    return render_to_response("university.html", data)
