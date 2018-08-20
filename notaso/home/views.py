from django.db.models import Count
from django.views.generic import TemplateView

from ..comments.models import Comment
from ..professors.models import Professor
from ..universities.models import University


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        if "view" not in kwargs:
            kwargs["view"] = self

        universities = University.objects.all()
        universities = list(universities)
        universities.sort(key=lambda x: x.get_grade())

        professors = (
            Professor.objects.annotate(num_comments=Count("comment"))
            .filter(score__gt=0, num_comments__gte=10)
            .order_by("-score")
        )

        comments = (
            Comment.objects.all().exclude(body__exact="").order_by("-created_at", "-id")
        )

        kwargs["professors"] = professors[:5]
        kwargs["universities"] = universities[:5]
        kwargs["recent_comments"] = comments[:5]
        kwargs["navbarSearchShow"] = True
        return kwargs
