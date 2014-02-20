from django.shortcuts import render_to_response, get_object_or_404

from .models import University

from departments.models import Department
from professors.models import Professor


def universities_view(request):
    data = {
        'universities': University.objects.all()
    }
    return render_to_response("universities.html", data)


def specific_university_view(request, slug):
    university = get_object_or_404(University, slug=slug)
    data = {
        'specified_university': university,
        'departments': Department.objects.all(),
        'professors': Professor.objects.filter(university=university),
        'grade' : university.get_grade()
    }
    return render_to_response("university.html", data)
