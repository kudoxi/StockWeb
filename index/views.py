from django.shortcuts import render
from django.http import HttpResponse,request
from time import sleep
from .tasks import start_running
import tushare as ts
import numpy as np
from datetime import datetime as dt
from stock.models import *
import logging
# Create your views here.
def index(req):
    #显示实时数据

    return render(req,'index.html')

def stock_basics(req):
    code = req.GET.get("code",'')
    code = req.GET.get("code")
    if not code:
        code = '1A0001'
    df = ts.get_stock_basics('')
    return HttpResponse(222)

#获取广告
def ads(req):
    return HttpResponse(222)

#获取股票数据
def stockinfo(req):
    print('>=====开始获取股票=====<')
    #stocklist = ts.get_stock_basics()
    dict = {}
    #print("code:",stocklist.index[0])
    #for i in range(len(stocklist['name'])):


    #for i in range(10):
    #    print('>>',end='')
    #    sleep(0.1)

    #start_running.delay()
    return HttpResponse('<h2> 请求已发送 </h2>')