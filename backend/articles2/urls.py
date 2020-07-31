from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.sign_in, name='register'),
    path('', views.index, name='index'),
]
