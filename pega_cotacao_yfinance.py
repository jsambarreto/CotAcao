import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

msft = yf.Ticker("MSFT")

# get historical market data
hist = msft.history(period="1d")

hist['Close'].plot(figsize=(16, 9))