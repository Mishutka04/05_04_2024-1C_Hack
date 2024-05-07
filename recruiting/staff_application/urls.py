from django.urls import path
from staff_application import views

app_name = 'staff'
urlpatterns = [
    path('', views.BaseTemplateForStaff.as_view(), name='base_for_staff'),
    path('resume_list', views.ResumeListView.as_view(), name='resume_list'),
    path('check_resume/<int:pk>/', views.ResumeUserCheckListView.as_view(), name='resume_user'),
    path('add_comment/<int:pk>/', views.AddCommentView.as_view(), name='add_comment'),
    path('resume_stage/<str:stage>/', views.ResumeStageView.as_view(), name='resume_stage'),
    path('resume_rejection/<int:pk>/', views.RejectionResumeView.as_view(), name='resume_rejection'),
    path('resume_new_stage/<int:pk>/', views.NewStageResumeView.as_view(), name='resume_new_stage'),
]
