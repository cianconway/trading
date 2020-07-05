import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'NXLN4QF9U7G9875O'

ts = TimeSeries(key=api_key, output_format='pandas')
data, metadata = ts.get_intraday(
    symbol='MSFT', interval='1min', outputsize='full')

print(data)

i = 1

# while i == 1:
#     data, metadata = ts.get_intraday(
#         symbol='MSFT', interval='1min', outputsize='full')
#     data.to_excel("trading_output.xlsx")
#     time.sleep(60)


close_data = data['4. close']
percent_change = close_data.pct_change()

print(percent_change)

last_change = percent_change[-1]
