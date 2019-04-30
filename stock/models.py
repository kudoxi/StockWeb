from django.db import models

# Create your models here.
INDUSTRIES = (
    (0,'未选择'),
    (1,'金融类'),
    (2,'重工业'),
    (3,'生物制药'),
    (4,'建筑施工'),
    (5,'电气设备'),
    (6,'软件服务'),
    (7,'专用机械'),
    (8,'化工原料'),


)
class Stock(models.Model):
    code = models.CharField(max_length=64,verbose_name="股票编号",null=True)
    name = models.CharField(max_length=64,verbose_name="公司名",null=True)
    industry = models.CharField(max_length=64,verbose_name="细分行业",null=True)#models.IntegerField(choices=INDUSTRIES,verbose_name="细分行业",default=0)
    area = models.CharField(max_length=64,verbose_name="地区",null=True)
    pe = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="市盈率")
    outstanding = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="流通股本")
    totals = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="总股本")
    totalAssets = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="总资产")
    liquidAssets = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="流通资产")
    fixedAssets = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="固定资产")
    reserved = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="公积金")
    reservedPerShare = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="每股公积金")
    esp = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="每股收益")
    bvps = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="每股净资")
    pb = models.DecimalField(max_digits=20,decimal_places=2,verbose_name="市净率")
    timeToMarket = models.DateTimeField(verbose_name="上市日期",auto_now_add=True)


    def __str__(self):
        return self.code


    class Meta:
        verbose_name = "股票"
        verbose_name_plural = verbose_name

#股票资讯
class StockNews(models.Model):
    title = models.CharField(max_length=64,verbose_name='标题')
    link = models.URLField(verbose_name='链接')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "股票资讯"
        verbose_name_plural = verbose_name