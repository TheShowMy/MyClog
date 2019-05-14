from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail
from django.http import JsonResponse
import json
from django.core import serializers
from django.contrib.auth import logout#注销session
from .models import BBSSecion,BBSReply,BBSTopic,BBSUsers
# Create your views here.


# def emil(request):
#     send_mail('Ty','','18308131833@163.com',{'lfw1357298341@126.com'},fail_silently=False,html_message='<h1>柠檬</h1>')
#     return HttpResponse('发出成功')

def index(request):
        return render(request,'app_user/index.html')
# 登录视图
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        users = BBSUsers.objects.filter(UName=user)
        if users.exists():
            if users[0].UPassword == password:
                userID = users[0].id
                request.session["username"] = userID
                print(userID)
                request.session.set_expiry(7200)  # 设置session寿命 值为0是默认关闭 浏览器消失
                return redirect('/')
            else:
                ztm = '账号或者密码错误!!!'
                return render(request,'app_user/login.html',locals())
        else:
            ztm = '账号不存在,请检查是否错误,或者创建一个账号'
            return render(request,'app_user/login.html',locals())
    else:
        return render(request,'app_user/login.html')


# 获取板块
def get_secion(request):
    secions = BBSSecion.objects.all()
    sec = {}
    for i, secion in enumerate(secions):
         sec[i] = {'SName':secion.SName,'SMasterID':secion.SMasterID.id,'SStatement':secion.SStatement,'SClickConut':secion.SClickConut,'STopicConut':secion.STopicConut}
    # sec = serializers.serialize('json', secions)[1:-1]
    # secions = json.loads(sec)
    return JsonResponse(sec)


# 获取登录的用户
def get_user(request):
    UID=request.session.get('username')
    if UID == None:
        sum = {'UName':'游客','zt':'登录','xw':'/login/'}
        return JsonResponse(sum)
    else:
        users = BBSUsers.objects.filter(id = UID)
        sum = {}
        for i, user in enumerate(users):
            sum = {'UName':user.UName,'zt':'注销','xw':'/logout/'}
        return JsonResponse(sum)


# 注销登录
def Ulogout(request):
    logout(request)
    return redirect('/')

