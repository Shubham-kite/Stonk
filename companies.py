import numpy as np 
import pandas as pd 
from datetime import date
from datetime import timedelta
import matplotlib.pyplot as plt
import yfinance as yf

start = date.today() - timedelta(days = 7)
end = date.today()
def tcs():
    tcs = yf.download('TCS',start,end)
    tcs[['Open','Close']].plot(label="TCS")
    plt.show()
def MSFT():
    MSFT = yf.download('MSFT',start,end)
    MSFT[['Open','Close']].plot(label="Microsot Opning and closing")
    plt.show()
def DE():
    DE = yf.download("D. E. Shaw & Co",start,end)
    DE[['Open','Close']].plot(label="D. E. Shaw & Co")
    plt.show()   