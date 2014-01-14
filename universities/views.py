from django.shortcuts import render_to_response
from models import Universities
from departments.models import Department
# Create your views here.
def universities_view(request):
	args = {}
	args['universitiesOnStorage'] = Universities.objects.all()
	return render_to_response("universities.html", args)

def specific_university_view(request, university_id = 1):
	args = {}
	args['specifiedUniversity'] = Universities.objects.get(id = university_id)
	args['departments'] = Department.objects.all()
	return render_to_response("university.html", args)

