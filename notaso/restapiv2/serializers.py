from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ..comments.models import Comment
from ..departments.models import Department
from ..professors.models import Professor
from ..universities.models import University


class UniversityListSerializer(serializers.HyperlinkedModelSerializer):
    grade = serializers.ReadOnlyField(source="get_grade")
    professors_count = serializers.ReadOnlyField(source="count")
    emblem = serializers.ImageField(use_url=False)

    class Meta:
        model = University
        fields = (
            "id",
            "name",
            "slug",
            "url",
            "city",
            "emblem",
            "grade",
            "professors_count",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class UniversityRetrieveSerializer(serializers.ModelSerializer):
    grade = serializers.ReadOnlyField(source="get_grade")
    professors_count = serializers.ReadOnlyField(source="count")
    departments = serializers.SerializerMethodField()
    extra_info = serializers.SerializerMethodField()
    emblem = serializers.ImageField(use_url=False)

    def get_departments(self, university):
        request = self.context.get("request", None)
        department_slug = request.GET.get("department")
        queryset = Department.objects.all()
        context = {"request": request, "university": university}
        if department_slug:
            department = get_object_or_404(queryset, slug=department_slug)
            serializer = DepartmentRetrieveSerializer(
                instance=department, context=context
            )
        else:
            serializer = DepartmentSerializer(
                instance=queryset, many=True, context=context
            )
        return serializer.data

    def get_extra_info(self, university):
        extra_info = {}
        request = self.context.get("request", None)
        context = {"request": request}
        professors = Professor.objects.filter(
            university=university, score__gt=0
        ).select_related("university")
        comments = (
            Comment.objects.filter(professor__in=professors)
            .select_related("created_by")
            .exclude(body__exact="")
            .order_by("-created_at", "-id")[:5]
        )
        hi_professors = professors.order_by("-score")[:5]
        low_professors = professors.order_by("score")[:5]
        extra_info = {
            "hi_professors": ProfessorListSerializer(
                instance=hi_professors, context=context, many=True
            ).data,
            "low_professors": ProfessorListSerializer(
                instance=low_professors, context=context, many=True
            ).data,
            "recent_comments": CommentSerializer(instance=comments, many=True).data,
        }
        return extra_info

    class Meta:
        model = University
        fields = (
            "id",
            "name",
            "slug",
            "city",
            "emblem",
            "grade",
            "professors_count",
            "extra_info",
            "departments",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    professors_count = serializers.SerializerMethodField()

    def get_professors_count(self, department):
        university = self.context.get("university")
        professor = Professor.objects.filter(department=department)

        if university:
            queryset = professor.filter(university=university).count()
        else:
            queryset = professor.count()

        return queryset

    class Meta:
        model = Department
        fields = ("id", "name", "slug", "url", "professors_count")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class DepartmentRetrieveSerializer(serializers.ModelSerializer):
    professors_count = serializers.SerializerMethodField()
    professors = serializers.SerializerMethodField()

    def get_professors_count(self, department):
        university = self.context.get("university")
        professor = Professor.objects.filter(department=department)
        if university:
            queryset = professor.filter(university=university).count()
        else:
            queryset = professor.count()

        return queryset

    def get_professors(self, department):
        university = self.context.get("university")
        professor = Professor.objects.filter(department=department)
        request = self.context.get("request", None)

        if university:
            queryset = professor.filter(university=university)
            professors = ProfessorListSerializer(
                instance=queryset, context={"request": request}, many=True
            )
            return professors.data
        else:
            return []

    class Meta:
        model = Department
        fields = ("id", "name", "slug", "professors_count", "professors")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


# Professors Serializers
class ProfessorListSerializer(serializers.HyperlinkedModelSerializer):
    grade = serializers.ReadOnlyField(source="get_grade")
    university = serializers.StringRelatedField()
    department = serializers.StringRelatedField()

    class Meta:
        model = Professor
        fields = (
            "id",
            "url",
            "first_name",
            "last_name",
            "slug",
            "gender",
            "university",
            "department",
            "score",
            "grade",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class ProfessorRetrieveSerializer(serializers.HyperlinkedModelSerializer):
    grade = serializers.ReadOnlyField(source="get_grade")
    total_rates = serializers.SerializerMethodField()
    responsibility = serializers.ReadOnlyField(source="get_responsibility")
    personality = serializers.ReadOnlyField(source="get_personality")
    difficulty = serializers.ReadOnlyField(source="get_difficulty")
    workload = serializers.ReadOnlyField(source="get_workload")
    user_comments = serializers.SerializerMethodField()
    university = serializers.StringRelatedField()
    department = serializers.StringRelatedField()

    def get_total_rates(self, professor):
        count = Comment.objects.filter(
            professor=professor, responsibility__gt=0
        ).count()
        return count

    def get_user_comments(self, professor):
        queryset = (
            Comment.objects.filter(professor=professor.id)
            .exclude(body__exact="")
            .order_by("-created_at", "-id")
        )
        serializers = CommentSerializer(instance=queryset, many=True)
        return serializers.data

    class Meta:
        model = Professor
        fields = (
            "id",
            "first_name",
            "last_name",
            "slug",
            "gender",
            "university",
            "department",
            "score",
            "total_rates",
            "grade",
            "responsibility",
            "personality",
            "difficulty",
            "workload",
            "user_comments",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class CommentSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(
        format="%d/%m/%Y %H:%M", required=False, read_only=True
    )

    def get_created_by(self, comment):
        if comment.is_anonymous is True:
            return "Anonimo"
        else:
            return comment.created_by.get_full_name()

    class Meta:
        model = Comment
        fields = (
            "created_by",
            "body",
            "is_anonymous",
            "responsibility",
            "personality",
            "workload",
            "difficulty",
            "created_at",
        )
