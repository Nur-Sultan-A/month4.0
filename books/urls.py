from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.me_view, name='about_me'),
    path('authors/', views.random_view, name='authors'),
    path('time/', views.time_view, name='time'),
]