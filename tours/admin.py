from django.contrib import admin
from .models import Tour, Category, Review

# Register your models here.


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'category',
        'price',
        'rating',
        'includes',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'review_rating',
        'review_content',
        'writtenon',
    )

    ordering = ('writtenon',)


admin.site.register(Tour, TourAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
