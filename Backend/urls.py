"""equipments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from equapi import views
from rest_framework.authtoken import views as v
from rest_framework_jwt import views as jwtviews
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^equ/(?P<euser>\w{8})$',views.EquList.as_view()),#登录教师设备
    re_path(r'^equdetail/(?P<enum>\w{8})/$',views.EquDetail.as_view()),#设备信息
    re_path(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    re_path(r'^equ/user/(?P<user>\w{8})$',views.UserMes.as_view()),#个人资料
    re_path(r'^equ/people/$',views.UserList.as_view()),#通讯录
    # re_path(r'^api/auth/login/$',views.LoginViewSet),
    # re_path(r'^api/auth/loout/$',views.LogoutView.as_view()),
    path('api-token-auth/', v.obtain_auth_token),#drf管理员默认认证方式,这里仅做测试使用
    path('borrowin/',views.BorrowIn.as_view()),#借入设备查询
    path('borrowout/',views.BorrowOut.as_view()),#借出设备查询
    re_path(r'returnequ/(?P<equnum>\w{8})',views.ReturnEqu.as_view()),#归还设备
    path('jwt-auth/',jwtviews.obtain_jwt_token),#登录验证与权限控制
    re_path(r'^changepwd/(?P<user>\w{8})$',views.ChangePwd.as_view()),#更改密码
    re_path(r'^borrow/$',views.Borrow.as_view())#租用设备
]

