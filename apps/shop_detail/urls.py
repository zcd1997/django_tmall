
from django.conf.urls import url,include

from apps.shop_detail import views

urlpatterns = [
    url('detail/',views.detail,name='detail')
]
