from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Professor
from forms import AddProfessorForm
from comments.forms import AddCommentForm
from comments.models import Comments


def specific_professor_view(request, professor_id=1):
    data = {
        'specified_professor': get_object_or_404(Professor, id=professor_id),
        'comment_form': AddCommentForm(),
        'comments': Comments.objects.filter(professor=professor_id)
    }
    return render(request, 'professor.html', data)
    
@login_required(login_url='/login/')
def create_professor_view(request):
    if request.POST:
        form = AddProfessorForm(request.POST)
        if form.is_valid():
            professor_information = form.save_form(request.user)
            return HttpResponseRedirect('/professors/%s' % professor_information.id)
    else:
        form = AddProfessorForm()
    data = {
        'form': form
    }  
    return render(request, 'create-professor.html', data)

@login_required(login_url='/login/')
def post_comment(request, professor_id):
    form = AddCommentForm(request.POST or None)

    if form.is_valid():
        form.save_form(request, professor_id)
    
    return HttpResponseRedirect(reverse('professors:specified_professor', 
                                kwargs={'professor_id': professor_id}))
