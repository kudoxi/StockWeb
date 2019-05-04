from django.shortcuts import render
from django.http import HttpResponse,request
from datetime import datetime as dt
from stock.models import *
from django.core import serializers
from time import sleep
from .tasks import start_running
import tushare as ts
import numpy as np
import logging
import json
import pandas as pd

class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, dt.date):
            return o.strftime('%Y/%m/%d')

# Create your views here.
def index(req):
    #显示实时数据
    code = req.GET.get("code")
    if not code:
        code = '600266'
    params = {}
    params['code'] = code

    return render(req,'index.html',params)

def stock_basics(req):
    code = req.GET.get("code")
    print("code:",code)
    if not code:
        code = '600266'
    params = {}
    #查名称
    stock_name = Stock.objects.filter(code = code).values("name")
    if not stock_name:
        params['code'] = 202
        params['msg'] = '暂无数据'
    else:
        params['code'] = 101
        params['stock_name'] = '2013年上半年{}指数'.format(stock_name[0]['name'])
        params['short_name'] = stock_name[0]['name']+'指数'
        #查数据
        df = ts.get_hist_data(code)
        if type(df) != 'NoneType':

            pd.set_option('display.max_columns', None)
            pd.set_option('max_colwidth', 200)

            print(df.head(),df.info())
            #日期
            date = df.index
            date2 = np.array(date)
            dates = date2.tolist()
            params['date'] = dates

            #开盘，收盘，最低，最高
            data = df.iloc[:, [0, 2, 3, 1]]
            data2 = np.array(data)
            datas = data2.tolist()
            params['datas'] = datas

            #五日均线
            kernel = np.exp(np.linspace(-1, 0, 5))
            kernel = kernel[::-1]  # 核数组需要逆序
            kernel /= kernel.sum() #归一化
            closing_prices = df.iloc[:,2]
            closing_prices = np.array(closing_prices)
            sma54 = np.convolve(closing_prices, kernel, 'valid')
            sma54 = sma54.tolist()
            for i in range(5):
                sma54.insert(0, '')
            params['meansline'] = sma54

        else:
            print("df is none")
    return HttpResponse(json.dumps(params,ensure_ascii=False))

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