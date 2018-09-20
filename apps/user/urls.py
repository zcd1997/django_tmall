import xadmin
from django.conf.urls import url, include
from django.contrib import admin

from apps.user import views

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('logout/', views.logout_view, name='logout'),
    url('register/', views.register, name='register'),

]
