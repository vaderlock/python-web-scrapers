import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf 
# import pandas_datareader.data as web

style.use('ggplot')

pf = pd.read_csv('SPY.csv', parse_dates = True, index_col=0)
print(pf)

pf['Adj Close'].plot()
plt.show()
