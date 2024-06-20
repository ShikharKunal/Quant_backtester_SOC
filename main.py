import datetime
import matplotlib.pyplot as plt
from data_fetch import hist_data
from plot import plot_data


symbol = 'RELIANCE.NS'
start = '2024-06-01'
end = datetime.datetime.today().strftime('%Y-%m-%d')

data = hist_data(symbol, start, end)
plot_data(data)