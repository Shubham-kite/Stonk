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

df = (tcs['Open'])
plt.show()