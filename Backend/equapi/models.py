from django.db import models
from django.contrib.auth.models import AbstractBaseUser

#使用自定义的管理器
class EquipManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isDelete=False)#返回未逻辑删除的数据
#设备信息
class EquipInfo(models.Model):
    eunit = models.CharField(max_length=50)#领用单位
    enum = models.CharField(max_length=50,primary_key=True)#仪器编号
    ename = models.CharField(max_length=50)#仪器名称
    etype = models.CharField(max_length=50)#型号
    especs = models.CharField(max_length=50)#规格
    ecost = models.CharField(max_length=50)#单价
    euser = models.CharField(max_length=50)#领用人
    elocate = models.CharField(max_length=50)#存放地名称
    ecompany = models.CharField(max_length=50)#厂家
    efacnum = models.CharField(max_length=50)#出厂号
    epuchasedate = models.DateField(max_length=6)#购置日期
    estatus = models.CharField(max_length=50)#现状
    esbuject = models.CharField(max_length=50)#经费科目
    eusedir = models.CharField(max_length=50)#使用方向
    esource = models.CharField(max_length=50)#设备来源
    estordate = models.DateField(max_length=6)#入库时间
    esupplier = models.CharField(max_length=50)#供货商
    einvoicenum = models.CharField(max_length=50)#发票号
    eclassnum = models.CharField(max_length=50)#分类号
    eremarks = models.CharField(max_length=200)#备注
    epromethod = models.CharField(max_length=50)#采购形式
    eusernum = models.ForeignKey('UserInfo',max_length=50,on_delete=models.CASCADE)#人员编号
    isDelete = models.BooleanField(default=False)#逻辑删除
    class Meta:
        db_table = 'equipinfo'

class UserInfo(AbstractBaseUser):
    authority_identity = models.CharField(max_length=20)#身份
    celphone = models.CharField(max_length=20)#手机号
    email = models.CharField(max_length=30)#电子邮箱
    identity = models.CharField(max_length=20)#身份
    landline = models.CharField(max_length=20)#固定电话
    name  = models.CharField(max_length=20)#姓名
    phone_cornet = models.CharField(max_length=20)#短号
    sex = models.CharField(max_length=10)#性别
    student_number = models.CharField(max_length=20,primary_key=True)#编号
    password = models.CharField(default='123',max_length=12)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'celphone'
    class Meta:
        db_table = 'userinfo'


class BorrowUser(models.Model):
    equipname = models.CharField(max_length=50)
    equipnum = models.CharField(max_length=50)
    ownername = models.CharField(max_length=50)
    ownernum = models.CharField(max_length=50)
    borrowname = models.CharField(max_length=50)
    borrownum = models.CharField(max_length=50)
    starttime = models.DateField(max_length=6)
    endtime = models.DateField(max_length=6)
    isactive = models.BooleanField(default=True)
    class Meta:
        db_table = 'borrowuser'