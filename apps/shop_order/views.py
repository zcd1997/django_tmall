import datetime
import json
import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from apps.home.models import *


@csrf_exempt
def confirm(request):
    car_ids = request.POST.getlist('car_ids')
    return render(request,'confirm.html',json.dumps({'car_ids':car_ids}))


"""
#  结算--->提交订单--->生成订单  主表是订单表
从购物车界面把{ 总金额  选中的商品的属性(checked)  }传到后台

"""


def order(request):
    # order_code= f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S"){random.randint(1000,9999)}}'
    # order = Order(order_code=order_code)
    # order.save()
    # cars = ShopCar.objects.filter(car_id=0)
    # return render()
    pass
