from django.test import TestCase
# Create your tests here.
import numpy as np
import tushare as ts

df = ts.get_hist_data('600266')
kernel = np.exp(np.linspace(-1, 0, 5))
kernel = kernel[::-1]  # 核数组需要逆序
kernel /= kernel.sum() #归一化
closing_prices = df.iloc[:,2]
closing_prices = np.array(closing_prices)
sma54 = np.convolve(closing_prices, kernel, 'valid')
sma54 = sma54.tolist()

for i in range(5):
    sma54.insert(0,'')

print(sma54)

