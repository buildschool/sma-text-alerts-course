# import dependencies
import btalib

# Get Sqqq TA function
def get_ta(hist):
    sma50 = {}
    sma200 = {}
    rsi = {}
    try:
        sma50 = btalib.sma(hist, period=50)
        sma50 =  sma50.df
        sma200 = btalib.sma(hist, period=200)
        sma200 = sma200.df
        rsi = btalib.rsi(hist, period=14)
        rsi = rsi.df
    except:
        print("Error with sqqq ta")
        pass
    return {"sma50":sma50, "sma200":sma200, "rsi":rsi}