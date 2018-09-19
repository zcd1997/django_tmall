import xadmin
from django.conf.urls import url,include
from django.contrib import admin

from apps.home import views

urlpatterns = [
    url('admin/', xadmin.site.urls),
    # url('tmall/',include('tmall.urls'))
    url('^$',views.index),
    url('home/',include('apps.home.urls')),
    url('user/', include('apps.user.urls')),
    url('pay/', include('apps.shop_pay.urls')),
    url('order/', include('apps.shop_order.urls')),
    url('detail/', include('apps.shop_detail.urls')),
    url('car/', include('apps.shop_car.urls')),
    url('cate/', include('apps.cate_detail.urls')),
    url('search/', include('apps.search.urls')),

]
