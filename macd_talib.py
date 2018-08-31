#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cmd
import time
from time import time, sleep
import sys
from decimal import *
import time
import binance
import datetime
from datetime import datetime
from email.mime.text import MIMEText
import telebot
import pymysql
import talib as ta
import numpy
from talib.abstract import MACD

my_file = open("coins.txt", "rb")
for line in my_file:
        l = [i.strip() for i in line.decode().split(' ')]
        coin = l[0]
        last_24hr = binance.ticker_24hr("%s" % (coin))
        change_24hr = round (Decimal (last_24hr["priceChangePercent"]), 2)
        candles = binance.candlesticks('%s' % (coin), "5m" , "81")
        candleclose1 = float(candles[0][4])
        candleclose2 = float(candles[1][4])
        candleclose3 = float(candles[2][4])
        candleclose4 = float(candles[3][4])
        candleclose5 = float(candles[4][4])
        candleclose6 = float(candles[5][4])
        candleclose7 = float(candles[6][4])
        candleclose8 = float(candles[7][4])
        candleclose9 = float(candles[8][4])
        candleclose10 = float(candles[9][4])
        candleclose11 = float(candles[10][4])
        candleclose12 = float(candles[11][4])
        candleclose13 = float(candles[12][4])
        candleclose14 = float(candles[13][4])
        candleclose15 = float(candles[14][4])
        candleclose16 = float(candles[15][4])
        candleclose17 = float(candles[16][4])
        candleclose18 = float(candles[17][4])
        candleclose19 = float(candles[18][4])
        candleclose20 = float(candles[19][4])
        candleclose21 = float(candles[20][4])
        candleclose22 = float(candles[21][4])
        candleclose23 = float(candles[22][4])
        candleclose24 = float(candles[23][4])
        candleclose25 = float(candles[24][4])
        candleclose26 = float(candles[25][4])
        candleclose27 = float(candles[26][4])
        candleclose28 = float(candles[27][4])
        candleclose29 = float(candles[28][4])
        candleclose30 = float(candles[29][4])
        candleclose31 = float(candles[30][4])
        candleclose32 = float(candles[31][4])
        candleclose33 = float(candles[32][4])
        candleclose34 = float(candles[33][4])
        candleclose35 = float(candles[34][4])
        candleclose36 = float(candles[35][4])
        candleclose37 = float(candles[36][4])
        candleclose38 = float(candles[37][4])
        candleclose39 = float(candles[38][4])
        candleclose40 = float(candles[39][4])
        candleclose41 = float(candles[40][4])
        candleclose42 = float(candles[41][4])
        candleclose43 = float(candles[42][4])
        candleclose44 = float(candles[43][4])
        candleclose45 = float(candles[44][4])
        candleclose46 = float(candles[45][4])
        candleclose47 = float(candles[46][4])
        candleclose48 = float(candles[47][4])
        candleclose49 = float(candles[48][4])
        candleclose50 = float(candles[49][4])
        candleclose51 = float(candles[50][4])
        candleclose52 = float(candles[51][4])
        candleclose53 = float(candles[52][4])
        candleclose54 = float(candles[53][4])
        candleclose55 = float(candles[54][4])
        candleclose56 = float(candles[55][4])
        candleclose57 = float(candles[56][4])
        candleclose58 = float(candles[57][4])
        candleclose59 = float(candles[58][4])
        candleclose60 = float(candles[59][4])
        candleclose61 = float(candles[60][4])
        candleclose62 = float(candles[61][4])
        candleclose63 = float(candles[62][4])
        candleclose64 = float(candles[63][4])
        candleclose65 = float(candles[64][4])
        candleclose66 = float(candles[65][4])
        candleclose67 = float(candles[66][4])
        candleclose68 = float(candles[67][4])
        candleclose69 = float(candles[68][4])
        candleclose70 = float(candles[69][4])
        candleclose71 = float(candles[70][4])
        candleclose72 = float(candles[71][4])
        candleclose73 = float(candles[72][4])
        candleclose74 = float(candles[73][4])
        candleclose75 = float(candles[74][4])
        candleclose76 = float(candles[75][4])
        candleclose77 = float(candles[76][4])
        candleclose78 = float(candles[77][4])
        candleclose79 = float(candles[78][4])
        candleclose80 = float(candles[79][4])
        prices = [candleclose1,candleclose2,candleclose3,candleclose4,candleclose5,candleclose6,candleclose7,candleclose8,candleclose9,candleclose10,candleclose11,candleclose12,candleclose13,candleclose14,candleclose15,candleclose16,candleclose17,candleclose18,candleclose19,candleclose20,candleclose21,candleclose22,candleclose23,candleclose24,candleclose25,candleclose26,candleclose27,candleclose28,candleclose29,candleclose30,candleclose31,candleclose32,candleclose33,candleclose34,candleclose35,candleclose36,candleclose37,candleclose38,candleclose39,candleclose40,candleclose41,candleclose42,candleclose43,candleclose44,candleclose45,candleclose46,candleclose47,candleclose48,candleclose49,candleclose50,candleclose51,candleclose52,candleclose53,candleclose54,candleclose55,candleclose56,candleclose57,candleclose58,candleclose59,candleclose60,candleclose61,candleclose62,candleclose63,candleclose64,candleclose65,candleclose66,candleclose67,candleclose68,candleclose69,candleclose70,candleclose71,candleclose72,candleclose73,candleclose74,candleclose75,candleclose76,candleclose77,candleclose78,candleclose79,candleclose80]
        prices = numpy.array([candleclose1,candleclose2,candleclose3,candleclose4,candleclose5,candleclose6,candleclose7,candleclose8,candleclose9,candleclose10,candleclose11,candleclose12,candleclose13,candleclose14,candleclose15,candleclose16,candleclose17,candleclose18,candleclose19,candleclose20,candleclose21,candleclose22,candleclose23,candleclose24,candleclose25,candleclose26,candleclose27,candleclose28,candleclose29,candleclose30,candleclose31,candleclose32,candleclose33,candleclose34,candleclose35,candleclose36,candleclose37,candleclose38,candleclose39,candleclose40,candleclose41,candleclose42,candleclose43,candleclose44,candleclose45,candleclose46,candleclose47,candleclose48,candleclose49,candleclose50,candleclose51,candleclose52,candleclose53,candleclose54,candleclose55,candleclose56,candleclose57,candleclose58,candleclose59,candleclose60,candleclose61,candleclose62,candleclose63,candleclose64,candleclose65,candleclose66,candleclose67,candleclose68,candleclose69,candleclose70,candleclose71,candleclose72,candleclose73,candleclose74,candleclose75,candleclose76,candleclose77,candleclose78,candleclose79,candleclose80], numpy.float)
        macd, macdsignal, macdhist = ta.MACD(prices, fastperiod=12, slowperiod=26, signalperiod=9)
        print (macd)
        print (macdsignal)
