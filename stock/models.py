from django.db import models

# Create your models here.

class Stock(models.Model):
    stocknumber = models.CharField(max_length=64,verbose_name="股票编号")
    company_name = models.CharField(max_length=64,verbose_name="公司名")
    industry = models.CharField(max_length=64,verbose_name="细分行业")
    area = models.CharField(max_length=64,verbose_name="地区")
    pe = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="市盈率")
    outstanding = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="流通股本")
    totals = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="总股本")
    totalAssets = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="总资产")
    liquidAssets = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="流通资产")
    fixedAssets = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="固定资产")
    reserved = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="公积金")
    reservedPerShare = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="每股公积金")
    esp = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="每股收益")
    bvps = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="每股净资")
    pb = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="市净率")
    timeToMarket = models.DateTimeField(verbose_name="上市日期")



#股票资讯
class StockNews(models.Model):
    title = models.CharField(max_length=64,verbose_name='标题')
    link = models.URLField(verbose_name='链接')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')