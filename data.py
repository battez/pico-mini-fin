# https://www.makeuseof.com/stock-price-data-using-python/
# info https://algotrading101.com/learn/yfinance-guide/
# https://algotrading101.com/learn/yahoo-finance-api-guide/
import yfinance as yf
import pandas as pd
import time 
from datetime import datetime
output = ""

# keys of interest
# currentPrice

# see example in guide of algo -- several tcikers and recent at once
tickers_list = ['NOK', 'IEF'] # IEF is close to VUTY; in $ tho
tickers_data = dict()


for ticker in tickers_list:
    
    try:
        
        ticker_object = yf.Ticker(ticker)

        #convert info() output from dictionary to dataframe
        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
        temp.reset_index(inplace=True)
        temp.columns = ["Attribute", "Recent"]
        
        # add (ticker, dataframe) to main dictionary
        tickers_data[ticker] = temp

    except KeyError:
        output += "Ticker unknown error"

    except:
        output += "N/A, try later"


print (output)

print(tickers_data)

# wait some seconds to satisfy rate limiting
time.sleep(2) 








