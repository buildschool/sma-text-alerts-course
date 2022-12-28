# import dependencies
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import yfinance as yf

# Get market data
def get_data(stock):
    stock = yf.Ticker(stock)
    hist = stock.history(interval="1m", period="1wk")
    return hist