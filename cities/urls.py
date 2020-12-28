from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('population-chart/', views.population_chart, name='population-chart'),
    path('city-chart/', views.city_chart, name='city-chart')
]