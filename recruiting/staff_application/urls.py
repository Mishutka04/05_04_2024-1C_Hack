from django.urls import path
from staff_application import views


app_name = 'staff'
urlpatterns = [
    path('', views.BaseTemplateForStaff.as_view(), name='base_for_staff'),
    path('resume_list', views.ResumeListView.as_view(), name='resume_list'),
    ]