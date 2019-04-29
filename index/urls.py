from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'ads/', views.ads,name='ads'),
    url(r'stockinfo/', views.stockinfo,name='stockinfo'),

]