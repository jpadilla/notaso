from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from notaso.restapi import serializers

from ..comments.models import Comment
from ..departments.models import Department
from ..professors.models import Professor
from ..universities.models import University


# Rest Api University ViewSet
class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = University.objects.all().order_by("-emblem")
    serializer_class = serializers.UniversityListSerializer

    def retrieve(self, request, pk=None):
        """
        Retrieve a university by id.

        Optional parameters:
        extra_info - if this parameter is declared true it will provide extra
        information for the university like the 5 top/worst professors
        and the 5 recent comments.

        Example of how to use it:
        - www.notaso.com/api/universities/1?extra_info=true
        """
        queryset = University.objects.all()
        university = get_object_or_404(queryset, pk=pk)
        professors = Professor.objects.filter(
            university=university, score__gt=0
        ).select_related("university")
        comments = (
            Comment.objects.filter(professor__in=professors)
            .select_related("created_by")
            .exclude(body__exact="")
            .order_by("-created_at", "-id")[:5]
        )
        if request.GET.get("extra_info") == "true":
            values = []
            for i, comment in enumerate(comments):
                if comment.is_anonymous is False:
                    userData = {"name": comment.created_by.get_full_name()}
                else:
                    userData = {"name": "Anonymous"}

                data = {
                    "name": userData["name"],
                    "body": comment.body,
                    "is_anonymous": comment.is_anonymous,
                    "created_at": comment.created_at,
                    "difficulty": comment.difficulty,
                    "responsibility": comment.responsibility,
                    "personality": comment.personality,
                    "workload": comment.workload,
                }
                values.insert(i, data)

            values_high_professors = serializers.ProfessorListSerializer(
                professors.order_by("-score")[:5],
                many=True,
                context={"request": request},
            )
            values_low_professors = serializers.ProfessorListSerializer(
                professors.order_by("score")[:5],
                many=True,
                context={"request": request},
            )
            university.extra_info = {
                "hi_professors": values_high_professors.data,
                "low_professors": values_low_professors.data,
                "recent_comments": values,
            }
        else:
            university.extra_info = {
                "hi_professors": [],
                "low_professors": [],
                "recent_comments": [],
            }
        university.professors_count = university.count()
        university.grade = university.get_grade()
        university.departments = Department.objects.all().values
        serializer = serializers.UniversityRetrieveSerializer(university)
        return Response(serializer.data)


# Rest Api Professor ViewSet
class ProfessorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = serializers.ProfessorListSerializer

    def retrieve(self, request, pk=None):
        """
        Retrieve a professor by id.


        Optional parameters:
        comments - if this parameter is declared true it will provide the
        list of all the user comments from that professor.

        Example of how to use it:
        - www.notaso.com/api/universities/1?comments=true
        """
        professor = Professor.objects.get(pk=pk)
        # professor = get_object_or_404(queryset, pk=pk)
        professor.grade = professor.get_grade()
        professor.total_rates = Comment.objects.filter(
            professor=professor.id, responsibility__gt=0
        ).count()
        professor.responsability = professor.get_responsibility()
        professor.personality = professor.get_personality()
        professor.workload = professor.get_workload()
        professor.difficulty = professor.get_difficulty()
        professor.user_comments = []
        if request.GET.get("comments") == "true":
            comments = (
                Comment.objects.filter(professor=professor.id)
                .exclude(body__exact="")
                .order_by("-created_at", "-id")
            )
            if len(comments) != 0:
                values = []
                for i, comment in enumerate(comments):
                    if comment.is_anonymous is False:
                        userData = {"name": comment.created_by.get_full_name()}
                    else:
                        userData = {"name": "Anonymous"}
                    data = {
                        "name": userData["name"],
                        "body": comment.body,
                        "is_anonymous": comment.is_anonymous,
                        "created_at": comment.created_at,
                        "difficulty": comment.difficulty,
                        "responsibility": comment.responsibility,
                        "personality": comment.personality,
                        "workload": comment.workload,
                    }
                    values.insert(i, data)
                professor.user_comments = {
                    "total_comments": len(comments),
                    "entries": values,
                }
            else:
                professor.user_comments = {
                    "total_comments": len(comments),
                    "info": "No comments values.",
                }
        serializer = serializers.ProfessorRetrieveSerializer(professor)
        return Response(serializer.data)


# Rest Api Department ViewSet
class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

    def list(self, request):
        """
        Get list of all the departments in notaso.

        Optional parameters:
        university_id - if this parameter is set it will provide more depth
        information from that university department.

        Example of how to use it:
        - www.notaso.com/api/universities/?university_id=1
        """
        if request.GET.get("university_id"):
            university_id = request.GET.get("university_id")
            for i, query in enumerate(self.queryset):
                if query.count(university_id) is not 0:
                    query.extra_info = {
                        "university_id": university_id,
                        "professors_count": query.count(university_id),
                        "rates": query.get_grade(university_id),
                    }
                else:
                    query.extra_info = {
                        "info": "No extra information"
                        + " in this university department."
                    }

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Get a department by id.

        Optional parameters:
        university_id - if this parameter is set it will provide more
        depth information from that university department. - by
        default this paramaters is set to false.

        Example of how to use it:
        - www.notaso.com/api/universities/1?university_id=1
        """
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        if request.GET.get("university_id"):
            university_id = request.GET.get("university_id")
            if department.count(university_id) is not 0:
                department.extra_info = {
                    "university": university_id,
                    "professors_count": department.count(university_id),
                    "rates": department.get_grade(university_id),
                }
            else:
                department.extra_info = {
                    "info": "No extra information" + " in this university department."
                }
        else:
            department.extra_info = {}
        serializer = serializers.DepartmentSerializer(
            department, context={"request": request}
        )
        return Response(serializer.data)


# Rest Api Search ViewSet
class SearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Professor.objects.all().order_by("first_name", "last_name")
    serializer_class = serializers.SearchSerializer

    def list(self, request):
        """
        Search a professor by keyword.

        Optional parameters:
        q - This parameter will return the professor search.

        Example of how to use it:
        - www.notaso.com/api/search?q={keyword}
        """
        search_term = request.GET.get("q")
        if search_term:
            qs = Professor.objects.filter(search_index=search_term)
        else:
            qs = self.queryset[:10]

        # Switch between paginated or standard style responses
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
