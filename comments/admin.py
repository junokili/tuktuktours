from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment',
                    'writer',
                    'writtenon',)

    ordering = ('writtenon',)


admin.site.register(Comment, CommentAdmin)
