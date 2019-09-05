# from django.shortcuts import render
from equapi import serializers
from equapi.models import EquipInfo
from equapi.models import UserInfo
from django.http import Http404
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

"""
当前用户的设备清单
"""


class EquList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, euser, format=None):
        queryset = EquipInfo.objects.filter(eusernum=euser)
        s = serializers.EquipInfoSerializer(queryset, many=True)
        return Response(s.data)


"""
当前设备的详细信息
"""


class EquDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, enum, format=None):
        queryset = EquipInfo.objects.filter(enum=enum)
        s = serializers.EquipInfoSerializer(queryset, many=True)
        return Response(s.data)

"""
修改密码
"""

from django.contrib.auth.models import User


class ChangePwd(APIView):
    def post(self, request, user, format=None):
        u = User.objects.get(first_name=user)
        print(request.data)
        if u.check_password(request.data['oldpwd']):
            u.set_password(request.data['newpwd'])
            u.save()
            return Response("success")
        else:
            return Response("fail")


"""
个人资料
"""


class UserMes(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, user, format=None):
        queryset = UserInfo.objects.filter(student_number=user)
        s = serializers.UserInfoSerializer(queryset, many=True)

        return Response(s.data)


"""
借阅功能
"""

from .models import BorrowUser
class Borrow(APIView):

    def post(self, request, format=None):
        s = serializers.BorrowUserSerializer(data=request.data)
        flag = True
        try:
            isexist = BorrowUser.objects.get(equipnum=request.data['equipnum'])
        except:
            flag = False
        if flag:
            return Response('error:isexist')
        else:
            if s.is_valid():
                if request.data['ownernum'] == request.data['borrownum']:
                    return Response('error:isowner')
                else:
                    s.save()
                    return Response('success')
        return Response("error:other")

"""
借出查询
"""
class BorrowOut(APIView):
    def post(self, request,format=None):
        queryset = BorrowUser.objects.filter(ownernum=request.data['mynum'])
        s = serializers.BorrowUserSerializer(queryset, many=True)

        return Response(s.data)




"""
借入查询
"""
class BorrowIn(APIView):
    def post(self, request,format=None):
        queryset = BorrowUser.objects.filter(borrownum=request.data['mynum'])
        s = serializers.BorrowUserSerializer(queryset, many=True)

        return Response(s.data)



"""
归还设备
"""
class ReturnEqu(APIView):
    def delete(self,request,equnum,format=None):
        queryset = BorrowUser.objects.get(equipnum=equnum)
        queryset.delete()
        return Response("Deleted")



"""
通讯录
"""


# 将原生语句产生的列表形式变成字典形式
def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


class UserList(APIView):

    def get(self, request, format=None):
        """
        queryset = UserInfo.objects.all().order_by('name')
        使用原生sql语句查找通讯录列表，根据中文首字母排序
        因此考虑用  raw sql 方式。在django中执行自定义语句的时候，返回的结果是一个tuple ,并我不是我所期望的dict.
        当结果是tuple 时，在木板HTML页面，如果要取得数据，必须知道对应数据在结果集中的序号,用序号的方式去得到值。这样很不方便。
        """
        cursor = connection.cursor()
        cursor.execute("select * from userinfo ORDER BY CONVERT(name USING gbk)")
        queryset = dictfetchall(cursor)
        s = serializers.UserInfoSerializer(queryset, many=True)
        return Response(queryset)

    def post(self,request,format=None):
        queryset = UserInfo.objects.filter(name__contains=request.data['searchName'])
        s = serializers.UserInfoSerializer(queryset,many=True)
        return Response(s.data)
"""
重写验证逻辑（手机号登录）
"""

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


# 此处不再使用
# class CustomModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserInfo.objects.get(Q(student_number=username) | Q(celphone=username))
#
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None


from .serializers import UserInfoSerializer

"""
JWT认证返回用户信息
"""


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.first_name, #用户编号
        'name': user.last_name #用户姓名
    }