from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

from .models import University

from departments.models import Department
from professors.models import Professor


def universities_view(request):
    data = {
        'universities': University.objects.all()
    }
    return render_to_response("universities.html", data)


def specific_university_view(request, slug):
    hit = False
    for university in University.objects.all():
        if university.slug == slug:
            data = {
                'specified_university': get_object_or_404(University, id=university.id),
                'departments': Department.objects.all(),
                'professors': Professor.objects.all()
            }
            return render_to_response("university.html", data)
    if hit is False:
        raise Http404
