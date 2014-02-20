from django.shortcuts import render_to_response, get_object_or_404

from universities.models import University
from .models import Department


def department_view(request, slug, department_slug):
    uni = get_object_or_404(University, slug=slug)
    department = get_object_or_404(Department, slug=department_slug)
    data = {
        'specified_university' : uni,
        'specified_department' : department,   
        'grade' : department.get_grade(uni),
        }
    
    return render_to_response('department.html', data)
