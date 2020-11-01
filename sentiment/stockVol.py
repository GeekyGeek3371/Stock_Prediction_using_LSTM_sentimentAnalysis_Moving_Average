import csv
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import mpld3


df = pd.read_csv('../csv/INFY_Train.NS.csv', index_col = 0)
fig=plt.figure(figsize=(24, 13))
plt.plot(df['Volume'], color='black', label='Stock volume')
plt.title('stock prices')
plt.xlabel('time [days]')
plt.ylabel('price')
plt.legend(loc='best')


html_str = mpld3.fig_to_html(fig)
Html_file= open("infosysStockVol.html","w")
Html_file.write(html_str)
Html_file.close()