from rest_framework import serializers

from ..professors.models import Professor
from ..universities.models import University
from ..departments.models import Department


# University Serializers
class UniversityListSerializer(serializers.HyperlinkedModelSerializer):
    grade = serializers.Field(source='get_grade')
    professors_count = serializers.Field(source='count')

    class Meta:
        model = University
        fields = ('id', 'url', 'name', 'city', 'emblem',
                  'slug', 'grade', 'professors_count')


class UniversityRetrieveSerializer(serializers.ModelSerializer):
    grade = serializers.Field(source='grade')
    professors_count = serializers.Field(source='professors_count')
    departments = serializers.Field(source='departments')
    extra_info = serializers.Field(source='extra_info')

    class Meta:
        model = University
        fields = ('id', 'name', 'city', 'emblem', 'slug',
                  'grade', 'professors_count', 'departments',
                  'extra_info')
        lookup_field = 'slug'


# Professors Serializers
class ProfessorListSerializer(serializers.HyperlinkedModelSerializer):
    university_name = serializers.RelatedField(source='university')
    department_name = serializers.RelatedField(source='department')

    class Meta:
        model = Professor
        fields = ('id', 'url', 'first_name', 'last_name', 'gender',
                  'university_name', 'department_name', 'slug', 'score')


class ProfessorRetrieveSerializer(serializers.ModelSerializer):
    grade = serializers.Field(source='grade')
    total_rates = serializers.Field(source='total_rates')
    responsability = serializers.Field(source='responsability')
    personality = serializers.Field(source='personality')
    difficulty = serializers.Field(source='difficulty')
    workload = serializers.Field(source='workload')
    total_comments = serializers.Field(source='total_comments')
    user_comments = serializers.Field(source='user_comments')
    university_name = serializers.RelatedField(source='university')
    department_name = serializers.RelatedField(source='department')

    class Meta:
        model = Professor
        fields = ('id', 'first_name', 'last_name', 'gender', 'university_name',
                  'department_name', 'slug', 'score', 'total_rates',
                  'grade', 'responsability', 'personality', 'difficulty',
                  'workload', 'user_comments')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    extra_info = serializers.Field(source='extra_info')

    class Meta:
        model = Department
        fields = ('id', 'url', 'name', 'slug', 'extra_info')


# Search Serializer
class SearchSerializer(serializers.ModelSerializer):
    university_name = serializers.RelatedField(source='university')
    department_name = serializers.RelatedField(source='department')

    class Meta:
        model = Professor
        fields = ('id', 'first_name', 'last_name', 'gender', 'university_name',
                  'department_name', 'score', 'slug')
