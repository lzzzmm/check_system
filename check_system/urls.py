"""check_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from UserProfiles_app.views import CustomPasswordResetView, password_reset_from_key

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/password/reset/', CustomPasswordResetView.as_view(), name='CustomPasswordResetView'),
    path('accounts/', include('allauth.urls')),
    path('UserProfiles_app/', include('UserProfiles_app.urls')),
    path('', include('Work_Dao.urls')),
    path('Other_Dao/', include('Other_Dao.urls')),
    path('My_project', include('My_project.urls')),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        password_reset_from_key,
        name="account_reset_password_from_key",
    ),
]
