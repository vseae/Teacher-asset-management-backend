from rest_framework import serializers
from equapi import models
from rest_framework import exceptions
from django.contrib.auth import authenticate
from rest_framework import authentication
class EquipInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EquipInfo
        fields=(
            "eunit",
            "enum",
            "ename",
            "etype",
            "especs",
            "ecost",
            "euser",
            "elocate",
            "ecompany",
            "efacnum",
            "epuchasedate",
            "estatus",
            "esbuject",
            "eusedir",
            "esource",
            "estordate",
            "esupplier",
            "einvoicenum",
            "eclassnum",
            "eremarks",
            "epromethod",
            "eusernum",
            "isDelete"
        )

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields=(
                'authority_identity',
                'celphone',
                'email',
                'identity',
                'landline',
                'name',
                'phone_cornet',
                'sex',
                'student_number'

        )
# class LoginSerializer(serializers.Serializer):
#     """
#     用户登录序列化类
#     """
#     celphone = serializers.CharField(required=True, max_length=128)
#     password = serializers.CharField(required=True, max_length=100)
#
#     # attrs 为封装后的request
#
#     def validate(self, data):
#         celphone = data.get('celphone')
#         password = data.get('password')
#         if celphone and password:
#             # 用户名称、密码登录验证
#             user = authenticate(celphone=celphone, password=password)
#             if not user:
#                 msg = '不能登录'
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = '必须输入同时输入名称和密码'
#             raise serializers.ValidationError(msg, code='authorization')
#         data['user'] = user
#         return data
#
#     class Meta:
#         model = models.UserInfo
#         fields = ('celphone', 'password', 'token')
class BorrowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BorrowUser
        fields = '__all__'
