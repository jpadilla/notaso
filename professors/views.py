from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404

from models import Professor
from forms import AddProfessorForm
from comments.forms import AddCommentForm
from comments.models import Comments


def specific_professor_view(request, professors_slug):
    hit = False
    for professor in Professor.objects.all():
        if professor.slug == professors_slug:
            data = {
                'specified_professor': Professor.objects.get(id=professor.id),
                'comment_form': AddCommentForm(),
                'comments': Comments.objects.filter(professor=professor.id)
            }
            return render(request, 'professor.html', data)
    if hit is False:
        raise Http404

@login_required(login_url='/login/')
def create_professor_view(request):
    if request.POST:
        form = AddProfessorForm(request.POST)
        if form.is_valid():
            professor_information = form.save_form(request)
            return HttpResponseRedirect('/professors/%s' % professor_information.id)
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

    return HttpResponseRedirect(reverse('professors:specified_professor',
                                kwargs={'professors_slug': professors_slug}))
