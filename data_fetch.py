import yfinance as yf
import pandas as pandas
import datetime
def hist_data(symbol, start, end, timeframe = '1d'):
    data = yf.download(symbol, start= start, end= end, interval= timeframe)
    return data


#lets try
# data = hist_data('RELIANCE.NS', '2024-06-01', datetime.datetime.today().strftime('%Y-%m-%d'))
# print(data.head())