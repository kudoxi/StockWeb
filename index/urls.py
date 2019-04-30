from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'ads/', views.ads,name='ads'),
    url(r'stock_basics/', views.stock_basics,name='stock_basics'),

]