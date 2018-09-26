"""

"""

from django.db.models import Sum

from apps.home.models import ShopCar


def shop_count(request):
    car_count = 0
    if request.user.is_authenticated():
        car_count = ShopCar.objects.filter(uid_id=request.user.userprofile.uid, status=1).aggregate(
            sum=Sum('number')).get('sum')
        if car_count == None:
            car_count =0
    return {'car_count': car_count}