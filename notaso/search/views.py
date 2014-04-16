from django.views.generic import ListView
from django.db.models import Q

from ..professors.models import Professor


class SearchView(ListView):
    queryset = Professor.objects.all().order_by('-first_name', 'last_name')
    template_name = 'search.html'

    def get_context_data(self):
        context = super(SearchView, self).get_context_data()
        context.update({
            'search_term': self.request.GET.get('q', ''),
            'navbarSearchShow': True
        })

        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        search_term = self.request.GET.get('q')

        if search_term:
            qs = Professor.objects.all()
            for term in search_term.split():
                qs = qs.filter(
                    Q(first_name__istartswith=term) |
                    Q(first_name__icontains=term) |
                    Q(last_name__istartswith=term) |
                    Q(last_name__icontains=term))
            return qs

        return queryset[:10]
