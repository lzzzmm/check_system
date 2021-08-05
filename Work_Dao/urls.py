from django.urls import path

from Work_Dao import views

urlpatterns = [
    path('profile/', views.profile.as_view(), name='profile'),
    path('update_note/<int:id>/', views.update_note, name='update_note'),
    path('delete_note/<int:id>/', views.delete_note, name='delete_note'),
    path('Task_list_wait/', views.Task_list_wait.as_view(), name='Task_list_wait'),
    path('Task_detail/<int:pk>/', views.Task_detail.as_view(), name="Task_detail"),
    path('update_task_detail/', views.update_task_detail, name='update_task_detail'),
    path('Task_history/', views.Task_history.as_view(), name='Task_history'),
    path('delete_task_history/<int:id>/', views.delete_task_history, name='delete_task_history'),
    path('Add_apply/', views.Add_apply, name='Add_apply'),
    path('Apply_history/', views.Apply_history, name='Apply_history'),
    path('delete_apply/<int:id>/', views.delete_apply, name='delete_apply'),
    path('apply_detail/<int:pk>/', views.apply_detail.as_view(), name='apply_detail'),
    path('update_apply/<int:id>/', views.update_apply, name='update_apply'),




]
