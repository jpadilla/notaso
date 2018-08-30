from django.contrib import admin

from .models import Professor


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "gender", "university", "department")
    search_fields = [
        "first_name",
        "last_name",
        "university__name",
        "department__name",
        "university__city",
    ]


admin.site.register(Professor, ProfessorAdmin)
