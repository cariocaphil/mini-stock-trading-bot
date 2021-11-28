import alpaca_trade_api as tradeapi
import numpy as np
import time

SEC_KEY = 'bcO995J1nB2W7iWbzIkXv4foX0GKaQJAYT8pX1fN'
PUB_KEY = 'PKRQE96HW8BM6TO9V13V'
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id=PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)

symb = "SPY"

while True:
    print("")
    print("Checking Price")

    # Get one bar object for each of the past 5 minutes
    market_data = api.get_barset(symb, 'minute', limit=5)

    close_list = []  # This array will store all the closing prices from the last 5 minutes
    for bar in market_data[symb]:
        # bar.c is the closing price of that bar's time interval
        close_list.append(bar.c)

    # Convert to numpy array
    close_list = np.array(close_list, dtype=np.float64)
    ma = np.mean(close_list)
    last_price = close_list[4]  # Most recent closing price

    print("Moving Average: " + str(ma))
    print("Last Price: " + str(last_price))

    time.sleep(60)  # Wait one minute before retreiving more market data
