import numpy as np 
import pandas as pd 
from datetime import date
from datetime import timedelta
import matplotlib.pyplot as plt
import yfinance as yf
from companies import *
'''downloading stocks data and displaying it '''
start = date.today() - timedelta(days = 7)
end = date.today()
Company = input("Enter Company name :").lower()
if(Company=='tcs'):
    tcs()
elif(Company=="microsoft"):
    MSFT()  
elif(Company=="de"):
    DE()