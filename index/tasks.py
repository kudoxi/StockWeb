from StockProject.celery import app
from time import sleep
import pandas as pd
import tushare as ts
from stock.models import  *
import numpy as np
from celery import shared_task
import logging
from datetime import datetime as dt
from stock.models import *
#同时启动：celery -A StockProject worker -B -l info
#

#################################　异步任务
## 单独启动：celery -A StockProject worker -l info
@app.task #shared_task
def start_running(nums):
    print('***>%s<***' %nums)
    print('--->>开始执行任务<<---')
    for i in range(10):
        print('>>'*(i+1))
        sleep(1)
    print('>---任务结束---<')

#################################　定时任务
# 单独启动：celery -A StockProject beat -l info
#
@app.task(name='deploy.tasks.get_stockinfo')
def get_stockinfo():
    print("开始存入")
    stocklist = ts.get_stock_basics()
    for i in range(len(stocklist['name'])):
        print(stocklist.index[i])
        dict2 = {}
        res = Stock.objects.filter(code=stocklist.index[i])
        useful_column = ['code','name','industry','industry','area','pe','outstanding','totals','totalAssets','liquidAssets',
                         'fixedAssets','reserved','reservedPerShare','esp','bvps','pb','timeToMarket']
        if not res.exists():
            for k, v in enumerate(stocklist):
                dict2['code'] = stocklist.index[i]
                if v in useful_column:
                    if v == 'timeToMarket':
                        #时间的特殊处理
                        string = str(stocklist[v][i])
                        stlist = list(string)
                        if len(stlist) == 8:
                            newlist = np.insert(stlist, [4, 6], ['-', '-'])
                            new_str = "".join(newlist)
                            ft = dt.strptime(new_str, '%Y-%m-%d')
                            dict2[v] = ft
                    else:
                        dict2[v] = stocklist[v][i]

            Stock.objects.create(**dict2)


    '''
        
    MyModel.objects.create(**data_dict)
    name industry area      pe  outstanding  totals  totalAssets  liquidAssets  fixedAssets  reserved  ...  bvps    pb  timeToMarket       undp  perundp    rev  profit    gpr   npr   holders
code                                                                                                       ...                                                                                    
300772   N运达     电气设备   浙江   75.70         0.73    2.94    657106.19     430567.56     55779.23  31323.65  ...  4.41  2.13      20190426   37977.80     1.29   0.00    0.00  16.60  1.34  138344.0
601789  宁波建工     建筑施工   浙江   23.68         9.76    9.76   1481910.63    1294265.75     91240.80  51575.03  ...  2.73  1.80      20110816  107892.35     1.11  11.70    7.72   7.66  1.40   44157.0
300292  吴通控股     软件服务   江苏   51.61        10.30   12.75    356974.75     124035.02     28526.73  88094.02  ...  2.18  3.06      20120229   58954.45     0.46  14.21  -24.01  20.89  5.75   63589.0
300202  聚龙股份     专用机械   辽宁  145.26         4.11    5.50    235927.27     175276.00     29415.84  13589.50  ...  2.92  3.19      20110415   79086.38     1.44 -37.15   51.40  47.32  6.51   16383.0
300405  科隆股份     化工原料   辽宁   55.55         1.33    1.52    168389.17     114943.00     35281.70  52466.38  ...  5.57  2.10      20141030   13065.87     0.86  -3.44  266.30  17.33  4.08  
    '''
    print(stocklist.head(),stocklist.info())
