"""
URL configuration for vus_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import path, include, reverse_lazy
from recruiting import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls', namespace="profile")),
    path('user/', include('user_application.urls', namespace="user_application"))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


def pageNotFound(request, exception):
    return render(request, "user_application/404.html")


def pagehandler500(request, *args, **argv):
    return render(request, "user_application/404.html")


handler500 = pagehandler500
handler404 = pageNotFound
