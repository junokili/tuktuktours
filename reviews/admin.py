from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'review_content',
                    'review_rating', 'author',
                    'writtenon', 'image')

    ordering = ('writtenon',)


admin.site.register(Review, ReviewAdmin)
