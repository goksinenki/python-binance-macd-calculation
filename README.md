# python-binance-macd-calculation

MACD calculation is very important if you like to trade crypto. 

So, with that scripts you can calculate MACD values in Binance and guess which coin will go UP/DOWN.

I have shared 2 ways to calculate it but I see that TALIB way is more trusted. So, I suggest you to use TALIB.

Here is a screenshot below. That shows what we are talking about.

![alt text](https://github.com/goksinenki/python-binance-macd-calculation/blob/master/macd.PNG)


INSTALLATION (Windows/Linux)

Installation

For Talib installation please check the URL below

https://github.com/afnhsn/TA-Lib_x64


How It Works

macd_talib.py will read the file coins.txt and connect to Binance get 5min period candlesticks data and make a list of last 80 candleclose prices values.

Then it calculates macd values with the help of TALIB formula for that values.

And you can get macd, signals and history values at the end.


Have a nice Trades :) !
