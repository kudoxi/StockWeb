from .models import *
from StockProject.celery import app
from django.db.models import F

#查看是否有买家匹配
def check_buyer(user,stockNo,price,price_range,hold):
    #查询是否有买家挂单
    buy_stock = BOSStock.objects.filter(
        stock_code = stockNo,
        role=1,
        price__range=(price,price+price_range)
    )
    #如果没有买家挂单
    if len(buy_stock)<=0:
        #卖家挂单
        bosstock = BOSStock()
        bosstock.user = user
        bosstock.role = 1
        bosstock.price = price
        #...
        bosstock.save()#挂单
    else:
        for st in buy_stock:
            if amount >= st.amount:
                amount = amount - st.amount
                hold[0].amount = hold[0].amount - st.amount
                hold[0].frozen_amount = hold[0].frozen_amount - st.amount
                hold.save()
                fund = Fund.objects.filter(user_id=user.id)
                fund[0].money = fund[0].money + st.amount * st.price
                fund.save()

                buyer = Hold.objects.filter(user=st.user,stock_code=stockNo)
                if buyer:
                    #更新购买者的持仓数量
                    buyer = Hold.objects.filter(user = st.user,stock_code=stockNo).update(amount=F('amount')+st.amount)
                else:
                    #创建持仓
                    Hold.objects.create()
                    #购买者的钱包里的钱扣除
