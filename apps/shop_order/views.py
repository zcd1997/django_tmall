import datetime
import random

from django.shortcuts import render

# Create your views here.
from apps.home.models import *


def confirm(request):
    request.POST.get('car_id')

    return render(request,'confirm.html')


#  结算--->提交订单--->生成订单  主表是订单表
def order(request):
    order_code= f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S"){random.randint(1000,9999)}}'
    order = Order(order_code=order_code)
    order.save()
    cars = ShopCar.objects.filter(car_id=0)
