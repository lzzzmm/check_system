from django.urls import path

from My_project import views

urlpatterns = [
    path('SignListView/', views.SignListView.as_view(), name='SignListView')
]
