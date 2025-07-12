from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createcar/', views.createcar, name='createcar'),
    path('createcarsave/', views.create_car_save, name='createcarsave'),
    path('readcar/', views.read_car, name='readcar'),
    path('updatecar/<int:car_id>/', views.update_car, name='updatecar'),
    path('deletecar/', views.delete_car, name='deletecar'),
    path('updatecarinput/', views.update_car_input, name='updatecarinput'),
    path('deletecarsave/', views.delete_car_save, name='deletecarsave'),
    path('searchcar/', views.search_car, name='searchcar'),
    path('help/', views.help_page, name='help'),
]