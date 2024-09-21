from django.contrib import admin
from django.urls import path
from tracking_app import views
from django.shortcuts import redirect

urlpatterns = [
    path('log_in/', views.log_in, name='login'),
    path('sign_up/', views.sign_up, name='signup'),
    path('', lambda request: redirect('signup')),
]
