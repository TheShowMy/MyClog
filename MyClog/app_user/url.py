from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'login/',views.login),
    url(r'logout/',views.Ulogout),#注销登录
    url(r'getsecion/',views.get_secion),#获取板块信息
    url(r'getuser/',views.get_user),#获取登录的用户信息

]