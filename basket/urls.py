from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<tour_id>/', views.add_to_basket, name='add_to_basket'),
    path('edit/<tour_id>/', views.edit_basket, name='edit_basket'),
    path('remove/<tour_id>/', views.remove_from_basket, name='remove_from_basket'),
]
