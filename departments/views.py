from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

from universities.models import University
from .models import Department


def department_view(request, slug, department_slug):
    university_hit = False
    for university in University.objects.all():
        if university.slug == slug:
            university_hit = True
            data = {
                'specified_university': get_object_or_404(University, id=university.id),
            }
    if university_hit is False:
        raise Http404
    department_hit = False
    for department in Department.objects.all():
        if department.slug == department_slug:
            department_hit = True
            data['specified_department'] = department
    if department_hit is False:
        raise Http404
    return render_to_response('department.html', data)
