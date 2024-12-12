"""Визначити URL шаблони для movierating."""
from django.urls import path

from . import views

app_name = 'movierating'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page where you make requests
    path('new_request/', views.new_request, name='new_request'),
    #Page with request result
    path('results/', views.results, name='results'),
]