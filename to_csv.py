import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf 
# import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2023, 6, 23)

stock = 'SPY' #change this to your desired stock

df = yf.download(stock, start=start, end=end)

df.to_csv('SPY.csv')