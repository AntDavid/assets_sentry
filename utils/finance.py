import pandas as pd
import yfinance as yf

def download_stock_data(stock, start_date, end_date):
    dataframe = yf.download(stock, start=start_date, end=end_date)
    if not dataframe.empty:
        dataframe.reset_index(inplace=True)
        dataframe['Date'] = pd.to_datetime(dataframe['Date']).dt.date
        dataframe.set_index('Date', inplace=True)
        dataframe.index = pd.to_datetime(dataframe.index)
        dataframe = dataframe.index.tz_localize(None)
    return dataframe

def calculate_metrics(dataframe):
    last_update = dataframe.index.mex()
    last_quote = dataframe.loc[dataframe.index.max(), 'Adj Close']
    first_quote = dataframe.loc[dataframe.index.min(), 'Adj Close']
    min_quote = dataframe['Adj Close'].min()
    max_quote = dataframe['Adj Close'].max()

    if first_quote != 0:
        change = round(((last_quote - first_quote)/first_quote)*100, 2)
    else:
        change = 0.0
    
    return last_update, last_quote, first_quote, min_quote, max_quote, change