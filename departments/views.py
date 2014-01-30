from django.shortcuts import render_to_response, get_object_or_404


from universities.models import Universities
from models import Department


def department_view(request, university_id, department_id):
    data = {
        "specified_university": get_object_or_404(Universities, id=university_id),
        "specified_department": get_object_or_404(Department, id=department_id)
    }
    return render_to_response('department.html', data)
