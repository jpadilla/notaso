from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from ..comments.forms import AddCommentForm
from ..comments.models import Comment
from .models import Professor
from .forms import AddProfessorForm


class ProfessorView(FormMixin, DetailView):
    model = Professor
    slug_url_kwarg = 'professors_slug'
    form_class = AddCommentForm
    template_name = 'professor.html'

    def get_success_url(self):
        return reverse(
            'professors:specified_professor',
            kwargs={'professors_slug': self.object.slug})

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self

        professor = get_object_or_404(
            Professor,
            slug=self.object.slug)
        kwargs['specified_professor'] = professor
        kwargs['comments'] = Comment.objects.filter(
            professor=professor.id).exclude(body__exact='')
        kwargs['rates'] = Comment.objects.filter(
            professor=professor.id, responsibility__gt=0).count()
        kwargs['grade'] = professor.get_grade()
        kwargs['responsability'] = professor.get_responsibility()
        kwargs['personality'] = professor.get_personality()
        kwargs['workload'] = professor.get_workload()
        kwargs['difficulty'] = professor.get_difficulty()
        return kwargs

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.save_form(self.request, self.object.slug)
        return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.get_form_class())
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# same as previous CBV
def specific_professor_view(request, professors_slug):
    professor = get_object_or_404(Professor, slug=professors_slug)
    form = AddCommentForm(request.POST or None)

    if request.user.is_authenticated and form.is_valid():
        form.save_form(request, professors_slug)
        return HttpResponseRedirect('/professors/%s' % professors_slug)

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
            specific_professor_view(request, professor_info.slug)
            return HttpResponseRedirect('/professors/%s' % professor_info.slug)
    else:
        form = AddProfessorForm()
    data = {
        'form': form
    }
    return render(request, 'create-professor.html', data)
