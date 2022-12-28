# sqqq direction function
def filter_ta(sqqq_ta, sqqq):
    sqqq_sma50 = {}
    sqqq_sma200 = {}
    sqqq_sma50 = sqqq_ta['sma50']
    sqqq_sma200 = sqqq_ta['sma200']
    # sqqq_rsi = sqqq_ta['rsi']
    if sqqq_sma50.iloc[-2]['sma'] < sqqq_sma200.iloc[-2]['sma']:
        if sqqq_sma50.iloc[-1]['sma'] < sqqq_sma200.iloc[-1]['sma']:
            # Bearish Bearish
            print("BEARISH BEARISH")
            # return "Death Cross Coninutation - HOLD SPY PUT on 15 Min TimeFrame"
            return "Death Cross Continuation - HOLD QQQ PUT on 1 Min TimeFrame"
        elif sqqq_sma50.iloc[-1]['sma'] > sqqq_sma200.iloc[-1]['sma']:
            # Bearish Bullish
            print("BEARISH BULLISH")
            return "Golden Cross - SELL QQQ PUT AND BUY QQQ CALL on 1 Min TimeFrame"
        else:
            print('Direction unconfirmed')
            return None
    elif sqqq_sma50.iloc[-2]['sma'] > sqqq_sma200.iloc[-2]['sma']:
        if sqqq_sma50.iloc[-1]['sma'] < sqqq_sma200.iloc[-1]['sma']:
            # Bullish Bearish
            print("BULLISH BEARISH")
            return "Death Cross - SELL CALL AND PUT SPY on 15 Min TimeFrame"
        elif sqqq_sma50.iloc[-1]['sma'] > sqqq_sma200.iloc[-1]['sma']:
            # Bullish Bullish
            print("BULLISH BULLISH")
            # return "Golden Cross Continuation - HOLD SPY CALL on 15 Min TimeFrame"
            return "Golden Cross Continuation - HOLD QQQ CALL on 1 Min TimeFrame"
        else:
            print('Direction unconfirmed')
            return None
    else:
        print('Direction unconfirmed')
        return None