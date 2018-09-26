from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from apps.user.context_processors import shop_count
from apps.home.models import *
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def add(request):
    # 判断是否是ajax请求
    if request.is_ajax():
        if request.user.is_authenticated():
            try:
                """
                参数  商品的数量
                参数  商品的id
                """
                uid = request.user.id
                shop_id = request.POST.get('shop_id')
                number = request.POST.get('number')
                """
                当商品已经存在用户的购物车的时候,更新数量
                当商品不存在用户的购物车的时候 创建该记录
               """
                cars = ShopCar.objects.filter(uid_id=uid, shop_id=shop_id, status=1)
                if cars:
                    car = cars.first()
                    #     表示存在就去更新
                    car.number = F('number') + number
                    # car.number += number
                    car.save(update_fields=['number'])
                else:
                    car = ShopCar(uid_id=uid, shop_id=shop_id, number=number)
                    car.save()
                    # 正常情况下返回json数据
                data = shop_count(request)
                data['status'] = 200
                data['msg'] = 'success'
                return JsonResponse(data=data)
            except Exception as e:
                # 表示添加购物车失败
                return JsonResponse(data={'status': 404, 'msg': 'error'})
        else:
            #  表示没有登录
            return redirect('/user/login/?next=%s' % request.path)
    else:
        return HttpResponse('错误的请求')


@csrf_exempt
def delete(request):
    try:
        car_id = request.POST.get('car_id')
        car = ShopCar.objects.get(car_id=car_id, status=1)
        car.status = -1
        car.save(update_fields=['status'])
        data = shop_count(request)
        data['status'] = 200
        data['msg'] = 'success'
        return JsonResponse(data=data)
    except:
        return JsonResponse({'status': 404, 'msg': 'error'})


# # 吐司
@csrf_exempt
def update_num(request):
    try:
        ac = request.POST.get('ac')
        car_id = request.POST.get('car_id')
        if ac == '1':
            count = ShopCar.objects.filter(car_id=car_id, status=1).update(number=F('number') + 1)
        else:
            # count = ShopCar.objects.filter(car_id=car_id, status=1).update(number=F('number') - 1)
            cars = ShopCar.objects.filter(car_id=car_id, status=1)
            car = cars.first().number
            if car > 1:
                count = cars.update(number=F('number') - 1)
        data = shop_count(request)
        data['status'] = 200
        data['msg'] = 'success'
        return JsonResponse(data=data)
    except Exception as e:
        return JsonResponse({'status': 404, 'msg': 'error'})


#
#
# # 减的操作
#
#
@login_required
def list(request):
    cars = ShopCar.objects.filter(uid=request.user.userprofile.uid, status=1)
    for car in cars:
        car.shop.image = car.shop.shopimage_set.all().first()
    return render(request, 'car.html', {'cars': cars})
