from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tours, name='tours'),
    path('<int:tour_id>/', views.indv_tour, name='indv_tour'),
    path('<int:tour_id>/make_review/', views.make_review,
         name='make_review'),
    path('<int:tour_id>/add_review/', views.add_review,
         name='add_review'),
    path('add/', views.add_tour, name='add_tour'),
    path('edit/<int:tour_id>', views.edit_tour, name='edit_tour'),
    path('delete/<int:tour_id>', views.delete_tour, name='delete_tour'),
    path('categories/', views.all_categories, name='categories'),
    path('categories/add_category/', views.add_category, name='add_category'),
    path('categories/edit_category/<int:category_id>',
         views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>',
         views.delete_category, name='delete_category'),
]
