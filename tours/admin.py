from django.contrib import admin
from .models import Tour, Category

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


admin.site.register(Tour, TourAdmin)
admin.site.register(Category, CategoryAdmin)
