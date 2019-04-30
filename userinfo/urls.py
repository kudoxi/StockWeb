from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/', views.login,name='login'),
    url(r'dologin/', views.dologin,name='dologin'),
    url(r'register/', views.register,name='register'),
    url(r'doregister/', views.doregister,name='doregister'),
    url(r'logout/', views.logout,name='logout'),
    url(r'usercenter/', views.usercenter,name='usercenter'),
    url(r'record/', views.record,name='record'),
    url(r'wallet/', views.wallet,name='wallet'),
    url(r'bankband/', views.bankband,name='bankband'),
    url(r'recharge/', views.recharge,name='recharge'),
    url(r'order/', views.order,name='order'),
    url(r'personal_stocklist/', views.personal_stocklist,name='pstocklist'),
    url(r'wantbuy/', views.wantbuy,name='wantbuy'),
    url(r'wantsell/', views.wantsell,name='wantsell'),

]