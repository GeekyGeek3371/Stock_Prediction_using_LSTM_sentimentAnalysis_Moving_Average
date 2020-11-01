import csv
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import mpld3


df = pd.read_csv('../csv/INFY_Train.NS.csv', index_col = 0)

#Calculating 30 days moving average
df['30_MA_Close'] = df['Close'].rolling(window=30).mean()
#calculating 20 days rolling standard devtaion
df['20_std_Close'] = df['Close'].rolling(window=20).std()

# Upper Bollinger Bands = Mean+2*SD
# Lower Bollinger Bands = Mean-2*SD
df['Upper'] = df['30_MA_Close'] + 2*df['20_std_Close']
df['Lower'] = df['30_MA_Close'] - 2*df['20_std_Close']

fig=plt.figure(figsize=(24, 13))
# plt.subplot(1,2,1)
plt.plot(df['Close'], color='black', label='Actual price')
plt.plot(df['Upper'], color='red', label='lower_band')
plt.plot(df['Lower'], color='green', label='higher_band')
plt.plot(df['30_MA_Close'], color='blue', label='movavg_close')

plt.title('stock prices')
plt.xlabel('time [days]')
plt.ylabel('price')
plt.legend(loc='best')

html_str = mpld3.fig_to_html(fig)
Html_file= open("infosys.html","w")
Html_file.write(html_str)
Html_file.close()

