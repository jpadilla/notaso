from django.shortcuts import render, get_object_or_404, redirect

from ..departments.models import Department
from ..professors.models import Professor
from ..comments.models import Comment
from ..universities.models import University

#rest api imports
from ..universities import serializers
from rest_framework import viewsets
from rest_framework.response import Response

#Serializer
from notaso.restapi import serializers


# Rest Api University ViewSet
class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = University.objects.all()
    serializer_class = serializers.UniversityListSerializer

    def list(self, request):
        '''
        Get list of all the universities in notaso.
        '''
        queryset = University.objects.all().order_by('-emblem')
        for university in queryset:
            university.grade = university.get_grade()
            university.professors_count = university.count()
        serializer = serializers.UniversityListSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        '''
        Retrieve a university by id.

        Optional params:
        extra_info - if this parameter is declared true it will provide extra
        information for the university like the 5 top/worst professors
        and the 5 recent comments.

        Example of how to use it:
        - www.notaso.com/api/universities/1?extra_info=true
        '''
        queryset = University.objects.all()
        university = get_object_or_404(queryset, pk=pk)
        professors = Professor.objects.filter(
            university=university,
            score__gt=0).select_related('university')
        comments = Comment.objects.filter(
            professor__in=professors).select_related('created_by').exclude(
                body__exact='').order_by('-created_at', '-id')[:5]
        if request.GET.get('extra_info') == "true":
            values = []
            for i, comment in enumerate(comments):
                if comment.is_anonymous is False:
                    userData = {'name': comment.created_by.get_full_name}
                else:
                    userData = {'name': "Anonymous"}
                data = {'name': userData['name'],
                        'body': comment.body,
                        'is_anonymous': comment.is_anonymous,
                        'created_at': comment.created_at,
                        'difficulty': comment.difficulty,
                        'responsibility': comment.responsibility,
                        'personality': comment.personality,
                        'workload': comment.workload}
                values.insert(i, data)
            university.extra_info = {
                'hi_professors': professors.order_by('-score')[:5].values,
                'low_professors': professors.order_by('score')[:5].values,
                'recent_comments': values}
        else:
            university.extra_info = {'hi_professors': [],
                                     'low_professors': [],
                                     'recent_comments': []}
        university.professors_count = university.count()
        university.grade = university.get_grade()
        university.departments = Department.objects.all().values
        serializer = serializers.UniversityRetrieveSerializer(university)
        return Response(serializer.data)


# Rest Api Professor ViewSet
class ProfessorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = serializers.ProfessorListSerializer

    def list(self, request):
        '''
        Get list of all the professors in notaso.
        '''
        professor = Professor.objects.all()
        serializer = serializers.ProfessorListSerializer(
            professor, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        '''
        Retrieve a professor by id.


        Optional params:
        comments - if this parameter is declared true it will provide the
        list of all the user comments from that professor.

        Example of how to use it:
        - www.notaso.com/api/universities/1?comments=true
        '''
        professor = Professor.objects.get(pk=pk)
        # professor = get_object_or_404(queryset, pk=pk)
        professor.grade = professor.get_grade()
        professor.total_rates = Comment.objects.filter(
            professor=professor.id, responsibility__gt=0).count()
        professor.responsability = professor.get_responsibility()
        professor.personality = professor.get_personality()
        professor.workload = professor.get_workload()
        professor.difficulty = professor.get_difficulty()
        professor.user_comments = []
        if request.GET.get('comments') == "true":
            comments = Comment.objects.filter(
                professor=professor.id).exclude(
                    body__exact='').order_by('-created_at', '-id')
            if len(comments) != 0:
                values = []
                for i, comment in enumerate(comments):
                    if comment.is_anonymous is False:
                        userData = {'name': comment.created_by.get_full_name}
                    else:
                        userData = {'name': "Anonymous"}
                    data = {'name': userData['name'], 'body': comment.body,
                            'is_anonymous': comment.is_anonymous,
                            'created_at': comment.created_at,
                            'difficulty': comment.difficulty,
                            'responsibility': comment.responsibility,
                            'personality': comment.personality,
                            'workload': comment.workload}
                    values.insert(i, data)
                professor.user_comments = {'total_comments': len(comments),
                                           'entries': values}
            else:
                professor.user_comments = {'total_comments': len(comments),
                                           'info': 'No comments values.'}
        serializer = serializers.ProfessorRetrieveSerializer(professor)
        return Response(serializer.data)


# Rest Api Department ViewSet
class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all().order_by('first_name', 'last_name')
    serializer_class = serializers.DepartmentSerializer

    def list(self, request):
        '''
        Get list of all the departments in notaso.

        Optional params:
        university_id - if this parameter is set it will provide more depth
        information from that university department.

        Example of how to use it:
        - www.notaso.com/api/universities/?university_id=1
        '''
        queryset = Department.objects.all()
        if request.GET.get('university_id'):
            university_id = request.GET.get('university_id')
            for i, query in enumerate(queryset):
                if query.count(university_id) is not 0:
                    query.extra_info = {
                        'university_id': university_id,
                        'professors_count': query.count(university_id),
                        'rates': query.get_grade(university_id)}
                else:
                    query.extra_info = {'info': 'No professors values.'}
        else:
            for i, query in enumerate(queryset):
                query.extra_info = {}

        serializer = serializers.DepartmentSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        '''
        Get a department by id.

        Optional params:
        university_id - if this parameter is set it will provide more
        depth information from that university department. - by
        default this paramaters is set to false.

        Example of how to use it:
        - www.notaso.com/api/universities/1?university_id=1
        '''
        queryset = Department.objects.all()
        department = get_object_or_404(queryset, pk=pk)
        if request.GET.get('university_id'):
            university_id = request.GET.get('university_id')
            if department.count(university_id) is not 0:
                department.extra_info = {
                    'university': university_id,
                    'professors_count': department.count(university_id),
                    'rates': department.get_grade(university_id)}
            else:
                department.extra_info = {'info': 'No professors values.'}
        else:
            department.extra_info = {}
        serializer = serializers.DepartmentSerializer(
            department, context={'request': request})
        return Response(serializer.data)


# Rest Api Search ViewSet
class SearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Professor.objects.all().order_by('first_name', 'last_name')
    serializer_class = serializers.SearchSerializer

    def list(self, request):
        '''
        Search a professor by keyword.

        Optional params:
        q - This parameter will return the professor search.

        Example of how to use it:
        - www.notaso.com/api/search?q={keyword}
        '''
        queryset = Professor.objects.all().order_by('first_name', 'last_name')
        search_term = request.GET.get('q')
        if search_term:
            print search_term
            for term in search_term.split():
                qs = Professor.objects.search(term, raw=True)
                serializer = serializers.SearchSerializer(
                    qs, context={'request': request}, many=True)
            return Response(serializer.data)
        else:
            queryset[:10]
            serializer = serializers.SearchSerializer(
                queryset, context={'request': request}, many=True)
            return Response(serializer.data)
