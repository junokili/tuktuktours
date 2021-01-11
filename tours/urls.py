from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tours, name='tours'),
    path('<int:tour_id>/', views.indv_tour, name='indv_tour'),
    path('add/', views.add_tour, name='add_tour'),
    path('edit/<int:tour_id>', views.edit_tour, name='edit_tour'),
    path('delete/<int:tour_id>', views.delete_tour, name='delete_tour'),
]
