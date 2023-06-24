import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import yfinance as yf 
# import pandas_datareader.data as web

style.use('ggplot')

pf = pd.read_csv('SPY.csv', parse_dates = True, index_col=0)

#100MA
pf['200ma'] = pf['Adj Close'].rolling(window=200, min_periods=0).mean()
pf.dropna(inplace=True) 

print(pf)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(pf.index, pf['Adj Close'])
ax1.plot(pf.index, pf['200ma'])
ax2.bar(pf.index, pf['Volume'])

plt.show()