from django.contrib import admin
from .models import BlogPost, Comment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'tour',
                    'createdon', 'image')
    search_fields = ['title', 'content']

    ordering = ('createdon',)


admin.site.register(BlogPost, BlogPostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', 'comment',
                    'writtenon',)

    ordering = ('writtenon',)


admin.site.register(Comment, CommentAdmin)
