from django.shortcuts import render_to_response
from django.http import Http404

from universities.models import Universities
from .models import Department


def department_view(request, slug, department_slug):
    university_hit = False
    for university in Universities.objects.all():
        if university.slug == slug:
            university_hit = True
            data = {
                'specified_university': Universities.objects.get(id=university.id),
            }
    if university_hit is False:
        raise Http404
    department_hit = False
    for department in Department.objects.all():
        if department.slug == department_slug:
            department_hit = True
            data['specified_department'] = Department.objects.get(id=department.id)
    if department_hit is False:
        raise Http404
    return render_to_response('department.html', data)
