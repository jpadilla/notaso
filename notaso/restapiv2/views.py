from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..departments.models import Department
from ..professors.models import Professor
from ..universities.models import University
from .filters import ProfessorFilter, UniversityFilter
from .serializers import (
    DepartmentSerializer,
    ProfessorListSerializer,
    ProfessorRetrieveSerializer,
    UniversityListSerializer,
    UniversityRetrieveSerializer,
)


class UniversityViewSet(ReadOnlyModelViewSet):
    """
    ### 1. Search Values
    > Search university by name keyword

    - ####Example:
        *  #####Search by University Name: [?search=Universidad de Puerto Rico](?search=Universidad de Puerto Rico)

    ---
    ### 2. Ordering Values
    > Order universities by id, name or city

    - ####Examples:
        *  #####Ordering by id: [?ordering=id](?ordering=id)
        *  #####Ordering by name: [?ordering=name](?ordering=name)
        *  #####Ordering by city: [?ordering=city](?ordering=city)

    The API may also specify reverse orderings by prefixing the field name
    with '-', like so:

     * #####Reverse ordering: [?ordering=-name](?ordering=id)

    Multiple orderings may also be specified:

     * #####Multiple ordering: [?ordering=name,city](?ordering=name,city)

    ---
    ### 3. Filters Values
    > Filters university by name or city.

    - ####Examples:
        *  #####Filter by name: [?name=Universidad de Puerto Rico](?name=Universidad de Puerto Rico)
        *  #####Filter by city: [?city=San Juan](?city=San Juan)
    ---
    ##Retrieve professors by university departments
    ---
    ###1. Professors list by university department
    > Search professors from an university by departments

    **Only works retrieving one university, doesn't work for university list.**

    - ####Example:
        *  #####Department slug: [?department=ciencias-de-computadora](?department=ciencias-de-computadora)

    ---
    """

    queryset = University.objects.all()
    serializer_class = UniversityListSerializer
    filter_backends = (
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    ordering_fields = ("id", "name", "city")
    search_fields = ("name",)
    filterset_class = UniversityFilter
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        university = get_object_or_404(University, slug=slug)
        serializer = UniversityRetrieveSerializer(
            university, context={"request": request}
        )
        return Response(serializer.data)


class ProfessorViewSet(ReadOnlyModelViewSet):
    """
    ### 1. Search Values
    > Search professors by name keywords

    - ####Example:
        *  #####Search by Name: [?search=Jose](?search=Jose)

    ---
    ### 2. Ordering Values
    > Order professors by id, first_name, last_name, score,
      university name, university city and department name

    - ####Examples:
        *  #####Ordering by id: [?ordering=id](?ordering=id)
        *  #####Ordering by first name: [?ordering=first_name](?ordering=first_name)
        *  #####Ordering by last name: [?ordering=last_name](?ordering=last_name)
        *  #####Ordering by score: [?ordering=score](?ordering=score)
        *  #####Ordering by university name: [?ordering=university__name](?ordering=university__name)
        *  #####Ordering by university city: [?ordering=university__city](?ordering=university__city)
        *  #####Ordering by department name: [?ordering=department__name](?ordering=department__name)

     The API may also specify reverse orderings by prefixing the field name
     with '-', like so:

     * #####Reverse ordering: [?ordering=-first_name](?ordering=-first_name)

    Multiple orderings may also be specified:

     * #####Multiple ordering: [?ordering=first_name,last_name](?ordering=first_name,last_name)

    ---
    ###3. Filters Values
    > Filters professors by name, university name,
    universitycity, department name, gender or score.

    - ####Examples:
        *  #####Filter by university name: [?university_name=Universidad de Puerto Rico](?university_name=Universidad de Puerto Rico)
        *  #####Filter by university_city: [?university_city=San Juan](?university_city=San Juan)
        *  #####Filter by department name: [?department=Ciencias de Computadora](?department=Ciencias de Computadora)
        *  #####Filter by gender: [?gender=M](?gender=M)
        *  #####Filter by score: [?score=90](?score=90)

    ---
    """

    queryset = Professor.objects.all()
    serializer_class = ProfessorListSerializer
    filter_backends = (
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    ordering_fields = (
        "id",
        "first_name",
        "last_name",
        "score",
        "university__name",
        "university__city",
        "department__name",
    )
    search_fields = ("first_name", "last_name")
    filterset_class = ProfessorFilter
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        professor = get_object_or_404(self.queryset, slug=slug)
        serializer = ProfessorRetrieveSerializer(professor)
        return Response(serializer.data)


class DepartmentViewSet(ReadOnlyModelViewSet):
    """
    ### 1. Search Values
    > Search departments by name keywords

    - ####Example:
        *  #####Search by University Name: [?search=Ciencias de Computadora](?search=Ciencias de Computadora)
    ---
    ### 2. Ordering Values
    > Order departments by id or name

    - ####Examples:
        *  #####Ordering by id: [?ordering=id](?ordering=id)
        *  #####Ordering by name: [?ordering=name](?ordering=name)

    The API may also specify reverse orderings by prefixing the field name
    with '-', like so:

     * #####Reverse ordering: [?ordering=-name](?ordering=-name)

    Multiple orderings may also be specified:

     * #####Multiple ordering: [?ordering=id,name](?ordering=id,name)

    ---
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = (
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    )
    ordering_fields = ("id", "name")
    search_fields = ("name",)
    lookup_field = "slug"
