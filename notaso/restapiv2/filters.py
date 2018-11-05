import django_filters

from ..professors.models import Professor
from ..universities.models import University


class UniversityFilter(django_filters.FilterSet):
    """
    Filter by University city
    """

    class Meta:
        model = University
        fields = ["name", "city"]


class ProfessorFilter(django_filters.FilterSet):
    """
    Filter professors by university name,
    university city, department and score.
    """

    university_name = django_filters.CharFilter(field_name="university__name")
    university_city = django_filters.CharFilter(field_name="university__city")
    department = django_filters.CharFilter(field_name="department__name")

    class Meta:
        model = Professor
        fields = ["university_name", "university_city", "department", "gender", "score"]
