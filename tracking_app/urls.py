from django.contrib import admin
from django.urls import path
from tracking_app import views
from django.shortcuts import redirect

urlpatterns = [
    path('log_in/', views.log_in, name='login'),
    path('sign_up/', views.sign_up, name='signup'),
    path('tasks_list/', views.tasks_list, name='tasks_list'),
    path('tasks_from_you/', views.tasks_from_you, name='tasks_from_you'),
    path('creating_task/', views.creating_task, name='creating_task'),
    path('view_task/<int:task_id>/',views.view_task, name='view_task'),
    path('changing_task/<int:task_id>/',views.changing_task, name='changing_task'),
    path('', lambda request: redirect('signup')),
]
