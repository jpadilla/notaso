from django.shortcuts import render_to_response
from universities.models import Universities
from models import Department
# Create your views here.
def department_view(request, university_id, department_id):
	args = {}
	args['specificUniversity'] = Universities.objects.get(id = university_id)
	args['specificDepartment'] = Department.objects.get(id = department_id)
	return render_to_response('department.html', args)