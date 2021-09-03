import numpy as np 
import pandas as pd 
from pandas.plotting import scatter_matrix
import datetime
import matplotlib.pyplot as plt
import yfinance as yf

'''downloading stocks data and displaying it '''
start = '2019-01-01'
end  = '2020-12-31'
tcs = yf.download('TCS',start,end)
infy = yf.download('INFY',start,end)
wipro = yf.download('WIPRO.NS',start,end)
tcs['Open'].plot(label = 'TCS', figsize = (15,7))
infy['Open'].plot(label = "Infosys")
wipro['Open'].plot(label = 'Wipro')
plt.title('Stock Prices of TCS, Infosys and Wipro')
