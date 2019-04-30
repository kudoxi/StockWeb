from django.db import models
from stock.models import *
from django.contrib.auth.models import AbstractUser

BANK = (
    (0, '中国银行'),
    (1, '中国工商银行'),
    (2, '中国建设银行')
)

# Create your models here.


class UserInfo(AbstractUser):
    #username = models.CharField(max_length=64,verbose_name='用户名')
    #password = models.CharField(max_length=64,verbose_name='密码')
    uphone = models.CharField(max_length=32,verbose_name='手机')
    uemail = models.EmailField(verbose_name='邮箱')
    isActive = models.BooleanField(default=True,verbose_name='是否激活')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')


    def __str__(self):
        return self.username


    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

#持仓表
class Hold(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name='持有用户')
    stock = models.ForeignKey(Stock,verbose_name="持有股票")
    amount = models.IntegerField(verbose_name="持有数量")
    frozen_amount = models.IntegerField(verbose_name="冻结数量")#对挂单的股票数量进行冻结

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "持仓"
        verbose_name_plural = verbose_name

# 钱包表
class Fund(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name="用户")
    money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="资金")
    frozen_money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="冻结资金")


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "钱包"
        verbose_name_plural = verbose_name

# 银行表
class Bank(models.Model):
    turename = models.CharField(max_length=64, verbose_name="真实姓名",null=True)
    user = models.ForeignKey(UserInfo, verbose_name="用户")
    bank = models.IntegerField(choices=BANK, verbose_name="银行",null=True)
    bankNo = models.CharField(max_length=64,verbose_name="银行卡号",null=True)
    password = models.CharField(max_length=255, verbose_name="支付密码",null=True)


    def __str__(self):
        return self.turename

    class Meta:
        verbose_name = "银行"
        verbose_name_plural = verbose_name
#发帖
class BlogType(models.Model):
    name = models.CharField(max_length=64,verbose_name='博客类型')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "发帖类型"
        verbose_name_plural = verbose_name

class Blog(models.Model):
    title = models.CharField(max_length=64,verbose_name='标题')
    details = models.TextField(verbose_name='内容')
    datetime = models.DateTimeField(verbose_name='发帖日期',auto_now_add=True)
    user = models.ForeignKey(UserInfo,verbose_name='发帖人')
    type = models.ForeignKey(BlogType,verbose_name='类型')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "发帖"
        verbose_name_plural = verbose_name

#自选股表--类似购物车
class SelfStock(models.Model):
    user = models.ForeignKey(UserInfo,verbose_name="用户")
    stock = models.ForeignKey(Stock,verbose_name="股票")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "自选股"
        verbose_name_plural = verbose_name