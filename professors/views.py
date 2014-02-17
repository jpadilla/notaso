from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Professor
from .forms import AddProfessorForm

from comments.forms import AddCommentForm
from comments.models import Comment


def specific_professor_view(request, professors_slug):
    professor = get_object_or_404(Professor, slug=professors_slug)
    data = {
        'specified_professor': professor,
        'comment_form': AddCommentForm(),
        'comments': Comment.objects.filter(professor=professor.id),
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
            professor_information = form.save_form(request)
            return HttpResponseRedirect('/professors/%s' % professor_information.slug)
    else:
        form = AddProfessorForm()
    data = {
        'form': form
    }
    return render(request, 'create-professor.html', data)


@login_required(login_url='/login/')
def post_comment(request, professors_slug):
    form = AddCommentForm(request.POST or None)

    if form.is_valid():
        form.save_form(request, professors_slug)
        professor = get_object_or_404(Professor, slug=professors_slug)
        comments = Comment.objects.filter(professor=professor.id).count()
        if form.cleaned_data.get('responsibility') != 0:
            professor.responsibility = responsibility_score(form, professor, comments)
            professor.save()
        if form.cleaned_data.get('personality') != 0:
            professor.personality = personality_score(form, professor, comments)
            professor.save()
        if form.cleaned_data.get('workload') != 0:
            professor.workload = workload_score(form, professor, comments)
            professor.save()
        if form.cleaned_data.get('difficulty') != 0:
            professor.difficulty = difficulty_score(form, professor, comments)
            professor.save()

    return HttpResponseRedirect(reverse('professors:specified_professor',
                                kwargs={'professors_slug': professors_slug}))


def responsibility_score(form, professor, comments):
    return (professor.responsibility + form.cleaned_data.get('responsibility'))/(comments*5)


def personality_score(form, professor, comments):
    return (professor.personality + form.cleaned_data.get('personality'))/(comments*5)


def workload_score(form, professor, comments):
    return (professor.workload + form.cleaned_data.get('workload'))/(comments*5)


def difficulty_score(form, professor, comments):
    return (professor.difficulty + form.cleaned_data.get('difficulty'))/(comments*5)
