from django.urls import path
from authentication import views

app_name = 'user_application'

urlpatterns = [
    path('create/', views.LoginUser.as_view(), name='login'),

]

