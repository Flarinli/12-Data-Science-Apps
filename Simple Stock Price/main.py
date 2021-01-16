import yfinance as yf
import streamlit as st
from matplotlib import pyplot as plt


st.write("""
# Simple Stock Price App
## Historical data
## (Shown the historical data from 2010-01-01 to 2021-01-01 about gold!)
""")


#define the ticker symbol
tickerSymbol = 'GOLD'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2021-1-1')

# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write('### Open')
st.line_chart(tickerDf.Open)
st.write('### High')
st.line_chart(tickerDf.High)
st.write('### Low')
st.line_chart(tickerDf.Low)
st.write('### Close')
st.line_chart(tickerDf.Close)
st.write('### Volume')
st.line_chart(tickerDf.Volume)
st.write('### Dividends')
st.bar_chart(tickerDf.Dividends)
