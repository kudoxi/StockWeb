from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import logging
import json
from django.core import serializers
# Create your views here.
def login(req):
    return HttpResponse("111")

def dologin(req):
    pass

def register(req):
    pass

def doregister(req):
    pass

def logout(req):
    pass

#个人中心
def usercenter(req):
    pass

#交易记录
def record(req):
    pass

#我的钱包
def wallet(req):
    pass

#ajax绑定银行卡
def bankband(req):
    if req.method == 'POST':
        user = req.POST.get('user')#模拟session里的user_id
        bank = req.POST.get('bank')
        bankNo = req.POST.get('bankNo')
        tradepwd = req.POST.get('tradepwd')
        truename = req.POST.get('truename')
        params = {}
        #密码在js端加密
        if user:
            try:
                Bank.objects.create(
                    user = user,
                    bank = bank,
                    bankNo = bankNo,
                    tradepwd = tradepwd
                )
            except Exception as e:
                logger = logging.getLogger('bankband')
                logger.error(e)
        else:
            params['error'] = '用户不存在'
            return HttpResponse(json.dumps(params))

#ajax一个模拟充值的接口，正式场景里要对接支付,这里只是往里面加钱，方便支付
def recharge(req):
    pass

#ajax自选股下单
def order(req):
    pass

#用户发起的购买和出售个人股票的列表页
def personal_stocklist(req):
    pass
#发起购买意向
def wantbuy(req):
    pass

#发起出售意向
def wantsell(req):
    pass



