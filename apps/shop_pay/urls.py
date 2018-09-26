from django.conf.urls import url,include

from apps.shop_pay import views

urlpatterns = [
    url('callback/',views.notify_callback)
]
