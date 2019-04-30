from django.db import models
from stock.models import *
from userinfo.models import *
# Create your models here.

ROLES = (
    (0,'卖家'),
    (1,'买家')
)
#挂单表
class BOSStock(models.Model):
    role = models.IntegerField(choices=ROLES,verbose_name='角色')
    stock = models.ForeignKey(Stock,verbose_name='股票')
    amount = models.IntegerField(verbose_name='操作数量')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='总价')
    user = models.ForeignKey(UserInfo,verbose_name='操作用户')
    datetime = models.DateTimeField(verbose_name='日期',auto_now_add=True)


    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = "挂单"
        verbose_name_plural = verbose_name

#交易记录表
class DealStock(models.Model):
    dealtime = models.DateTimeField(verbose_name="交易时间",auto_now_add=True)
    suser = models.ForeignKey(UserInfo,related_name="seller")
    buser = models.ForeignKey(UserInfo,related_name="buyer")
    stock = models.CharField(max_length=64,verbose_name='股票编号')
    amount = models.IntegerField(verbose_name='购买数量')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='购买总价')

    def __str__(self):
        return self.buser.username

    class Meta:
        verbose_name = "交易记录"
        verbose_name_plural = verbose_name