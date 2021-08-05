
from django.contrib import admin
from django.urls import path

from UserProfiles_app import views

urlpatterns = [
    path('mymessage/<int:pk>/', views.mymessage.as_view(), name='mymessage'),
    path('updatemessage/', views.updatemessage, name="updatemessage"),


]
