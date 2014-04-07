from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from ..comments.forms import AddCommentForm
from ..comments.models import Comment
from .models import Professor
from .forms import AddProfessorForm


def specific_professor_view(request, professors_slug):
    professor = get_object_or_404(Professor, slug=professors_slug)
    form = AddCommentForm(request.POST or None)

    if request.user.is_authenticated and form.is_valid():
        form.save_form(request, professors_slug)
        return HttpResponseRedirect('/professors/%s' % professors_slug)

    print professor.get_grade()
    data = {
        'specified_professor': professor,
        'comment_form': form,
        'comments': Comment.objects.filter(professor=professor.id)
        .exclude(body__exact=''),
        'rates': Comment.objects.filter(professor=professor.id,
        responsibility__gt=0).count(),
        'grade': professor.get_grade(),
        'responsability': professor.get_responsibility(),
        'personality': professor.get_personality(),
        'workload': professor.get_workload(),
        'difficulty': professor.get_difficulty()
    }

    return render(request, 'professor.html', data)


@login_required(login_url='/login/')
def create_professor_view(request):
    if request.POST:
        form = AddProfessorForm(request.POST)
        if form.is_valid():
            professor_info = form.save_form(request)
            return HttpResponseRedirect('/professors/%s' % professor_info.slug)
    else:
        form = AddProfessorForm()
    data = {
        'form': form
    }
    return render(request, 'create-professor.html', data)
