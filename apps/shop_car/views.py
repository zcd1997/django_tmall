from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
# 购物车功能
from django.views.decorators.csrf import csrf_exempt

from apps.home.models import ShopCar


@csrf_exempt
# @login_required  登录判断
def add(request):
    """
    参数  商品数量
    参数  商品的id
    当商品已存在购物车中时,更新数量
    当商品不存在购物车中时,创建该记录
    """
    if request.is_ajax():
        if request.user.is_authenticated():
            try:
                uid = request.user.userprofile.id
                shop_id = request.POST.get('shop_id')
                number = request.POST.get('number')
                car = ShopCar.objects.get(uid=uid, shop_id=shop_id, status=1)
                if car:
                    car.number = F('number') + number
                    car.save(update_fields=['number'])
                else:
                    car = ShopCar(uid=uid, number=number, status=1)
                    car.save()
                return
            except:
                pass
        else:
            return redirect('/user/login/?next%s'% request.path)
    else:
        return HttpResponse('错误的请求')
    def delete(request):
        pass

    def update_num(request):
        pass

    def find(request):
        pass


    def list(request):
        pass
