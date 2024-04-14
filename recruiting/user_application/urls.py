from django.urls import path
from user_application import views


app_name = 'user_application'

urlpatterns = [
    path('create/', views.CreateResume.as_view(), name='create_resume'),
    path('create/profession/<int:pk>', views.ProfessionView.as_view(), name='create_profession'),
    path('create/education/<int:pk>', views.EducationView.as_view(), name='create_education'),
    path('create/about/<int:pk>', views.AboutView.as_view(), name='create_about'),
    path('create/skills/<int:pk>', views.SkillsView.as_view(), name='create_skills'),
    path('create/languages/<int:pk>', views.LanguagesView.as_view(), name='create_languages'),
    path('create/course/<int:pk>', views.CourseView.as_view(), name='create_course'),
    path('list_resume', views.ResumeListView.as_view(), name='resume_list'),
    path('resume/<int:pk>', views.ResumeCheckListView.as_view(), name='check_resume')

]

