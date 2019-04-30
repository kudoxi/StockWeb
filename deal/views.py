from django.shortcuts import render

# Create your views here.
from .models import *
from datetime import datetime


#1判断是买还是卖
#2购买人是否有购买力，账户资金是否大于股票所需金额
#3资金不够提示无法购买,要求充值，或者直接进入页面时就给出提示
#资金够，挂出意向，并冻结这部分的资金
#4查询是否有符合的卖家

#5卖家出售时，查询是否有这么多股票;
#6持仓足够就冻结他的那些股票
#7撮合（
# celery 定时器循环查询记录表，一直没有匹配的卖家就一直挂单
# 对价格符合的买家和卖家进行撮合，
# 如果卖家出售数量大于买家购买数量，买家这边交易成功，并扣除卖家待售数量
# 　此时卖家还有剩余待出售，就挂单
# 如果卖家出售数量小于买家的购买数量，卖家这边交易成功，买家的购买数量减少）

#amount交易数量
#price_range:价格浮动范围内可交易
def deal(user,sob,stockNo,amount,price_range):
    result = {}
    if sob == 'seller':
        #当前持有股票
        hold = Hold.objects.filter(
            user_id = user.id ,stock_code = stockNo,
        )
        # 当前可售股票
        new_amount = hold[0].amount - hold[0].frozen_amount
        stock = Stock.objects.get(
            code = stockNo
        )
        datetimes = datetime.now()
        if new_amount >= amount:
            hold[0].frozen_amount = hold[0].frozen_amount + amount
            hold.save()

            result['msg'] = '股票已挂单'
            return

        else:
            result['msg'] = '所持有的股票数量不足'
            return