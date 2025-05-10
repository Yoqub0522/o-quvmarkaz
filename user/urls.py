from  django.urls import path
from django.contrib.auth import views as auth_views

from user.views import register, login_view, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('',auth_views.LoginView.as_view(template_name='login.html') , name='login'),

    path('logout/', logout_view, name='logout'),
]