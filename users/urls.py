from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.authloginView, name='login'),
    path('logout/', views.authLogoutView, name='logout'),
    path('user_list/', views.user_list_view, name='user_list'),
    path('verify-email/<uuid:token>/', views.verify_email, name='verify_email'),
]