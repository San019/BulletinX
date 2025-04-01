from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('submit/', views.submit_notice, name='submit_notice'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout , name='logout'),  # Built-in logout view
]