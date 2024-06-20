import matplotlib.pyplot as plt 


def plot_data(df):
    plt.figure(figsize = (10,5))
    plt.plot(df['Close'], label = 'Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Closing Prices')
    plt.legend()
    plt.show()


