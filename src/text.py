# import files/ dependencies
from functions import check_time
from functions import get_if_market_day
from functions import filter_ta
from functions import get_data
from functions import get_ta
from functions import send_text
from datetime import time

# define main
def main():
    qqq = get_data.get_data('QQQ')
    qqq_ta = get_ta.get_ta(qqq)
    body = filter_ta.filter_ta(qqq_ta, qqq)
    if body != None:
        send_text.send_text(body)

# Define time
current_time = check_time.check_time()

# check open
open = time(14,30)

# check close
close = time(21,0)

# define stock_market_open
stock_market_open = get_if_market_day.get_if_market_day()

# If market is open check holdings
if stock_market_open:
    if current_time > open:
        if current_time < close:
            main()
        else:
            print("After hours")
    else:
        print("Pre Market")
else:
    print('Market not open today')

# for testing
# main()