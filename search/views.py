import operator
from functools import reduce

from django.views.generic import ListView
from django.db.models import Q

from professors.models import Professor
from departments.models import Department
from universities.models import University


class SearchView(ListView):
    queryset = Professor.objects.all().order_by('-first_name', 'last_name')
    template_name = 'search.html'

    def get_context_data(self):
        context = super(SearchView, self).get_context_data()

        universities = University.objects.all().values_list('name', 'city').distinct()

        departments = Department.objects.all().values_list('name', flat=True).distinct()

        context.update({
            'universities': universities[:20],
            'departments': departments[:20],
            'search_term': self.request.GET.get('q', '')
        })

        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        search_term = self.request.GET.get('q')

        if search_term:
            search_args = []
            queries = (
                'first_name__istartswith',
                'last_name__istartswith',
                'last_name__icontains',
            )

            for term in search_term.split():
                for query in queries:
                    search_args.append(Q(**{query: term}))

            return queryset.filter(
                reduce(operator.or_, search_args)).distinct()[:10]

        return queryset[:10]
