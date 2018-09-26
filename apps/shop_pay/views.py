from django.shortcuts import render, redirect
from alipay import AliPay
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from django_tmall import settings


def pay(request):
    # 创建支付宝对象
    alipay = AliPay(
        appid=settings.APP_ID,
        app_notify_url='http://127.0.0.1:8000/pay/callback',
        app_private_key_string=settings.APP_PRIVATE_STRING,
        alipay_public_key_string=settings.APP_PUBLIC_STRING,
        debug=True
    )


    order_url = alipay.api_alipay_trade_page_pay(
            subject='测试',
            out_trade_no='666',
            total_amount='1.00',
            # 支付成功之后 前端套住啊你的界面get请求
            return_url='http://www.baidu.com',
            # 后台接收支付宝支付相关的信息的接口  post请求
            # notify_url =

    )
    pay_url = settings.ALI_PAY_DEV_URL + '?' + order_url
    return redirect()


@csrf_exempt
def notify_callback(request):
    pass
