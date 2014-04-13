from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'body', 'professor', 'created_by',)
    search_fields = ['body', 'professor__first_name', 'professor__last_name']

admin.site.register(Comment, CommentAdmin)
