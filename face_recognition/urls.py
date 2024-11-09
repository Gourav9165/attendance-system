from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register_student'),
    path('take-attendance/', views.take_attendance, name='take_attendance'),
    path('view-attendance/', views.view_attendance, name='view_attendance'),
]
