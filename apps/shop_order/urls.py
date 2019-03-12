import xadmin
from django.conf.urls import url, include
from django.contrib import admin

from apps.shop_order import views

urlpatterns = [
    url('confirm/', views.confirm, name='confirm')
]
