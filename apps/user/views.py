from django.contrib.auth import *
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from apps.home.models import ShopCar


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login_page.html')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login_page.html', {'msg': '用户名或密码错误'})
        except:
            return render(request, 'login_page.html', {'msg': '网络异常请重试'})
    else:
        return render(request, 'login_page.html', {'msg': '不支持的请求方式'})

def logout_view(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'GET':
        return render(request, 'register_page.html')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('password2')
            if password and username and password == confirm_password:
                users = User.objects.filter(username=username)
                if users:
                    return render(request, 'register_page.html', {'msg': '该用户已存在'})
                    # 注册账号已经存在
                else:
                    user = User.objects.create_user(username=username,password=password)
                    user.save()
                    #保存成功之后跳转到首页
                    return redirect('/')
            else:
                # 参数不符合要求
                return render(request,'register_page.html',{'msg':'参数不正确'})
        except:
            return render(request, 'register_page.html', {'msg': '网络异常请重试'})
    else:
        return render(request, 'register_page.html', {'msg': '不支持的请求方式'})
