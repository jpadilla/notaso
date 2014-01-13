from django.shortcuts import render_to_response
from models import Professor
# Create your views here.
def specific_professor_view(request, professor_id = 1):
	args ={}
	args['specifiedProfessor'] = Professor.objects.get(id = professor_id)
	return render_to_response('professor.html', args)
