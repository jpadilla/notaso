from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from import_export.admin import ImportExportModelAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User
from .resources import UserResource


class UserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_admin",
        "created_at",
        "modified_at",
    )
    list_filter = ("is_admin", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_admin", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
