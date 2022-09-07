#import the packages
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
#import the graphing packages
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

#set variables
firstdf = input("first ticker: ")
secondf = input("second ticker: ")
thirdf = input("third ticker: ")
#Set time parameters:
start = dt.datetime(2016,1,1)
end = dt.datetime(2021,12,31)
#Create a dataframe from downloaded data 
fdf = web.DataReader(firstdf, 'yahoo', start, end)
sdf = web.DataReader(secondf, 'yahoo', start, end)
tdf = web.DataReader(thirdf, 'yahoo', start, end)
#Export to a csv
fdf.to_csv('fdf.csv')
sdf.to_csv('sdf.csv')
tdf.to_csv('tdf.csv')
#Reset the dataframe variable to read the exported data with dates as the index:
fdf = pd.read_csv('fdf.csv', parse_dates=True, index_col=0)
sdf = pd.read_csv('sdf.csv', parse_dates=True, index_col=0)
tdf = pd.read_csv('tdf.csv', parse_dates=True, index_col=0)
#Reduce decimal places for easier viewing
pd.set_option("display.precision", 2)
#calculate 100 ma
fdf['100ma']= fdf['Adj Close'].rolling(window=100, min_periods =0).mean()
sdf['100ma']= sdf['Adj Close'].rolling(window=100, min_periods =0).mean()
tdf['100ma']= tdf['Adj Close'].rolling(window=100, min_periods =0).mean()
#style
style.use('dark_background')
close= fdf['Adj Close']
close2= sdf['Adj Close']
close3= tdf['Adj Close']
sma= fdf['100ma']
sma2= sdf['100ma']
sma3= tdf['100ma']

#First stock graph
plt.figure(figsize = (12,6))
ax1= plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan =1)
ax2= plt.subplot2grid((8,1), (6,0), rowspan = 1, colspan =1)
ax1.plot(fdf.index, fdf['Adj Close'], label='Adjusted Close')
ax1.plot(fdf.index, fdf['100ma'], label ='100 Day sma')
ax2.bar(fdf.index, fdf['Volume'])
ax1.set_title(firstdf.upper() + ' Stock Trends')
ax1.set_ylabel('Stock Price')
ax1.set_xlabel('Year')
ax1.legend()
ax2.set_title(firstdf.upper() + ' Moving Volume')
ax2.set_ylabel('Volume')
ax2.set_xlabel('Year')

#Second stock graph
plt.figure(figsize = (12,6))
ax1= plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan =1)
ax2= plt.subplot2grid((8,1), (6,0), rowspan = 1, colspan =1) 
ax1.plot(sdf.index, sdf['Adj Close'], label='Adjusted Close')
ax1.plot(sdf.index, sdf['100ma'], label ='100 Day sma')
ax2.bar(sdf.index, sdf['Volume'])
ax1.set_title(secondf.upper() + ' Stock Trends')
ax1.set_ylabel('Stock Price')
ax1.set_xlabel('Year')
ax1.legend()
ax2.set_title(secondf.upper() + ' Moving Volume')
ax2.set_ylabel('Volume')
ax2.set_xlabel('Year')

#Third stock graph graph
plt.figure(figsize = (12,6))
ax1= plt.subplot2grid((8,1), (0,0), rowspan = 5, colspan =1)
ax2= plt.subplot2grid((8,1), (6,0), rowspan = 1, colspan =1) 
ax1.plot(tdf.index, tdf['Adj Close'], label='Adjusted Close')
ax1.plot(tdf.index, tdf['100ma'], label ='100 Day sma')
ax2.bar(tdf.index, tdf['Volume'])
ax1.set_title(thirdf.upper() + ' Stock Trends')
ax1.set_ylabel('Stock Price')
ax1.set_xlabel('Year')
ax1.legend()
ax2.set_title(thirdf.upper() + ' Moving Volume')
ax2.set_ylabel('Volume')
ax2.set_xlabel('Year')


plt.show()