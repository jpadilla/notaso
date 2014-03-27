from django.shortcuts import render

from professors.models import Professor
from universities.models import University
from comments.models import Comment


def home(request):
    universities = University.objects.all()
    universities = list(universities)
    universities.sort(key=lambda x: x.get_grade())
    data = {
        'professors': Professor.objects.all().order_by('-score')[:5],
        'universities': universities[:5],
        'recent_comments': Comment.objects.all().exclude
        (body__exact='').order_by('-created_at')[:5],
    }

    return render(request, "home.html", data)
