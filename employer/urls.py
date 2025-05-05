from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.employer_register, name='employer_register'),
    path('login/', views.employer_login, name='employer_login'),
    path('dashboard/', views.dashboard, name='employer_dashboard'),
]
