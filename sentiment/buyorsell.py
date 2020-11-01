from infy_sentiment import *
from infy import *


ans=""
print(avgSent+todSent+mabs)
if(avgSent+todSent+mabs>=2):
    print("Buy")
elif(avgSent+todSent+mabs<-1):
    print("Sell")
else:
    print("Hold")
    ans="Hold"

