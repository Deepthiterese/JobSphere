from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='jobseeker_register'),
    path('login/', views.login_view, name='jobseeker_login'),
    path('logout/', views.logout_view, name='jobseeker_logout'),
    path('', views.home, name='jobseeker_home'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
]
