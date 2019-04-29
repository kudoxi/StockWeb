from django.db import models
import mongoengine
# Create your models here.
#class StockModel(mongoengine.Document):
#     name = mongoengine.StringField(max_length=32)
#     age = mongoengine.IntField(default=0)

class AdLink(models.Model):
    title = models.CharField(max_length=64,verbose_name='广告名')
    ad_img = models.ImageField(upload_to='static/ads',verbose_name='图片路径')
    ad_link = models.URLField(verbose_name='广告链接')
    isDelete = models.BooleanField(default=False,verbose_name='是否删除')





