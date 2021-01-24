from django.contrib import admin
from .models import Tour, Category, Review, Rating

# Register your models here.


class TourAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'duration',
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
        'review_emoji',
        'review_content',
        'writtenon',
    )

    ordering = ('writtenon',)


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'rating_name',
        'rating_number',
    )

    ordering = ('rating_number',)


admin.site.register(Tour, TourAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Rating, RatingAdmin)
