from django.shortcuts import render_to_response
from models import Professor
from users.models import UserProfile
from django.core.context_processors import csrf
from forms import AddProfessorForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
# Create your views here.
def specific_professor_view(request, professor_id = 1):
	args ={}
	args['specifiedProfessor'] = Professor.objects.get(id = professor_id)
	return render_to_response('professor.html', args)

@login_required(login_url='/register/login/')
def create_professor_view(request):
	if request.POST:
		form = AddProfessorForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			my_object = get_object_or_404(Professor, pk = 1)
			lastname = form.cleaned_data['lastname']
			my_object = get_object_or_404(Professor, pk = 1)
			gender = form.cleaned_data['gender']
			my_object = get_object_or_404(Professor, pk = 1)
			university = form.cleaned_data['university']
			my_object = get_object_or_404(Professor, pk = 1)
			department = form.cleaned_data['department']
			my_object = get_object_or_404(Professor, pk = 1)
			created_by = form.cleaned_data['created_by']
			my_object = get_object_or_404(Professor, pk = 1)
			form.save()
			return HttpResponseRedirect('/universities')
	else:
		form = AddProfessorForm()
   	args = {}
  	args.update(csrf(request))
   	
   	args['form'] = form
   	
   	return render_to_response('create-professor.html', args)
