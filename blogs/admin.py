from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',
                    'createdon', 'image')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    ordering = ('createdon',)


admin.site.register(BlogPost, BlogPostAdmin)
