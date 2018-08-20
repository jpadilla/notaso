from rest_framework import serializers

from ..departments.models import Department
from ..professors.models import Professor
from ..universities.models import University


# University Serializers
class UniversityListSerializer(serializers.HyperlinkedModelSerializer):
    grade = serializers.ReadOnlyField(source="get_grade")
    professors_count = serializers.ReadOnlyField(source="count")
    emblem = serializers.ImageField(use_url=False)

    class Meta:
        model = University
        fields = (
            "id",
            "url",
            "name",
            "city",
            "emblem",
            "slug",
            "grade",
            "professors_count",
        )


class UniversityRetrieveSerializer(serializers.ModelSerializer):
    grade = serializers.ReadOnlyField()
    professors_count = serializers.ReadOnlyField()
    departments = serializers.ReadOnlyField()
    extra_info = serializers.ReadOnlyField()
    emblem = serializers.ImageField(use_url=False)

    class Meta:
        model = University
        fields = (
            "id",
            "name",
            "city",
            "emblem",
            "slug",
            "grade",
            "professors_count",
            "departments",
            "extra_info",
        )
        lookup_field = "slug"


# Professors Serializers
class ProfessorListSerializer(serializers.HyperlinkedModelSerializer):
    university_name = serializers.StringRelatedField(source="university")
    department_name = serializers.StringRelatedField(source="department")

    class Meta:
        model = Professor
        fields = (
            "id",
            "url",
            "first_name",
            "last_name",
            "gender",
            "university_name",
            "department_name",
            "slug",
            "score",
        )


class ProfessorRetrieveSerializer(serializers.ModelSerializer):
    grade = serializers.ReadOnlyField()
    total_rates = serializers.ReadOnlyField()
    responsability = serializers.ReadOnlyField()
    personality = serializers.ReadOnlyField()
    difficulty = serializers.ReadOnlyField()
    workload = serializers.ReadOnlyField()
    user_comments = serializers.ReadOnlyField()
    university_name = serializers.StringRelatedField(source="university")
    department_name = serializers.StringRelatedField(source="department")

    class Meta:
        model = Professor
        fields = (
            "id",
            "first_name",
            "last_name",
            "gender",
            "university_name",
            "department_name",
            "slug",
            "score",
            "total_rates",
            "grade",
            "responsability",
            "personality",
            "difficulty",
            "workload",
            "user_comments",
        )


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    extra_info = serializers.ReadOnlyField()

    class Meta:
        model = Department
        fields = ("id", "url", "name", "slug", "extra_info")


# Search Serializer
class SearchSerializer(serializers.ModelSerializer):
    university_name = serializers.StringRelatedField(source="university")
    department_name = serializers.StringRelatedField(source="department")

    class Meta:
        model = Professor
        fields = (
            "id",
            "first_name",
            "last_name",
            "gender",
            "university_name",
            "department_name",
            "score",
            "slug",
        )
