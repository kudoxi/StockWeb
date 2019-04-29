from django.shortcuts import render
from django.http import HttpResponse,request
from time import sleep
from .tasks import start_running
import tushare as ts
# Create your views here.
def index(req):
    #df = ts.realtime_boxoffice()
    #print(df)
    #dg = ts.get_hist_data('000002')
    #print(dg)
    #return HttpResponse('index')
    return render(req,'index.html')

#获取广告
def ads(req):
    return HttpResponse(222)

#获取股票数据
def stockinfo(req):
    print('>=====开始获取股票=====<')
    stocklist = ts.get_stock_basics()
    for k,v in enumerate(stocklist):
        if k < 2:
            for k2 ,v2 in enumerate(stocklist[v]):
                if k2 <10:
                    print(k,k2,v,v2)
    #for i in range(10):
    #    print('>>',end='')
    #    sleep(0.1)

    #start_running.delay()
    return HttpResponse('<h2> 请求已发送 </h2>')