from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tours, name='tours'),
    path('<tour_id>', views.indv_tour, name='indv_tour'),
]
