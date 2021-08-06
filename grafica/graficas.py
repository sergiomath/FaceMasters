import pandas_datareader as web
import datetime as dt
import mplfinance as mpf
a = int(input("Introduce año de inicio: "))
m = int(input("Introduce mes de inicio: "))
d = int(input("Introduce dia de inicio: "))
x = input("Introduce accion a analizar: ")
start = dt.datetime(a, m, d)
end = dt.datetime.now()

# Altcoins also work
data = web.DataReader(x, "yahoo", start, end)

mpf.plot(data, type="candle", volume=True, style="yahoo")
bye = input("bye")