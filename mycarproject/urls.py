from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),  # pastikan cars/urls.py ada
]