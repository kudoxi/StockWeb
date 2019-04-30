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
    #stocklist = ts.get_stock_basics()
    dict = {}
    #print("code:",stocklist.index[0])
    #for i in range(len(stocklist['name'])):

    '''
    stocklist = ts.get_stock_basics()
    for i in range(len(stocklist['name'])):
        print(stocklist.index[i])
        dict2 = {}
        res = Stock.objects.filter(code=stocklist.index[i])
        if not res.exists():
            for k, v in enumerate(stocklist):
                if v == 'timeToMarket':
                    # 时间的特殊处理
                    string = str(stocklist[v][i])
                    stlist = list(string)
                    if len(stlist) == 8:
                        newlist = np.insert(stlist, [4, 6], ['-', '-'])
                        new_str = "".join(newlist)
                        ft = dt.strptime(new_str, '%Y-%m-%d')
                        dict2[v] = ft
                else:
                    dict2[v] = stocklist[v][i]
            # logger = logging.getLogger('django')
            # logger.info(dict2)
    '''
    #for i in range(10):
    #    print('>>',end='')
    #    sleep(0.1)

    #start_running.delay()
    return HttpResponse('<h2> 请求已发送 </h2>')