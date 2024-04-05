from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from authentication import views

app_name = 'profile'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('edit/', views.ProfileEdit.as_view(), name='edit'),
    path('profile/', views.ShowProfile.as_view()),
    path('', views.ShowProfile.as_view(), name='profile'),
]

