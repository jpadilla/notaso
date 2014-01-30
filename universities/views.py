from django.shortcuts import render_to_response, get_object_or_404

from models import Universities
from departments.models import Department


def universities_view(request):
    data = {
        'universities': Universities.objects.all()
    }
    return render_to_response("universities.html", data)


def specific_university_view(request, university_id=1):
    data = {
        'specified_university': get_object_or_404(Universities, id=university_id),
        'departments': Department.objects.all()
    }
    return render_to_response("university.html", data)
