from django.urls import path
from user_application import views


app_name = 'user_application'

urlpatterns = [
    path('create/', views.create_resume, name='create_resume'),
    path('create/2', views.create_resume_2, name='create_resume_2'),
    path('create/3', views.create_resume_3, name='create_resume_3'),
    path('create/4', views.create_resume_4, name='create_resume_4'),
]

