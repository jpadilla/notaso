from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView
from django.views.generic.edit import FormMixin

from braces.views import LoginRequiredMixin

from ..comments.forms import AddCommentForm
from ..comments.models import Comment
from .forms import AddProfessorForm
from .models import Professor


class ProfessorView(FormMixin, DetailView):
    model = Professor
    slug_url_kwarg = "professors_slug"
    form_class = AddCommentForm
    template_name = "professor.html"

    def get_context_data(self, **kwargs):
        if "view" not in kwargs:
            kwargs["view"] = self

        professor = get_object_or_404(Professor, slug=self.object.slug)

        kwargs["user_rates"] = Comment.objects.filter(
            created_by=self.request.user.id, professor=professor, responsibility__gt=0
        ).count()

        kwargs["specified_professor"] = professor
        kwargs["comments"] = (
            Comment.objects.filter(professor=professor.id)
            .exclude(body__exact="")
            .order_by("-created_at", "-id")
        )
        kwargs["rates"] = Comment.objects.filter(
            professor=professor.id, responsibility__gt=0
        ).count()
        kwargs["grade"] = professor.get_grade()
        kwargs["responsability"] = professor.get_responsibility()
        kwargs["personality"] = professor.get_personality()
        kwargs["workload"] = professor.get_workload()
        kwargs["difficulty"] = professor.get_difficulty()
        return kwargs

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.save_form(self.request, self.object.slug)
        return redirect(
            "professors:specified_professor", professors_slug=self.object.slug
        )

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form(self.get_form_class())
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CreateProfessorView(LoginRequiredMixin, FormView):
    form_class = AddProfessorForm
    template_name = "create-professor.html"

    def form_valid(self, form):
        prof = form.save_form(self.request)
        return redirect("professors:specified_professor", professors_slug=prof.slug)
