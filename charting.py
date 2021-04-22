import datetime as dt
import streamlit as st
import pandas_datareader as pdr


def charting(ticker):
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2021, 5, 1)
    tickerdf = pdr.get_data_yahoo(ticker, start, end)

            # working with data
    tickerdf['MA10'] = tickerdf['Close'].rolling(10).mean()
    tickerdf['EMA10'] = tickerdf['Close'].ewm(span=10, adjust=False).mean()
    exp1 = tickerdf['Close'].ewm(span=12, adjust=False).mean()
    exp2 = tickerdf['Close'].ewm(span=26, adjust=False).mean()
    tickerdf['MACD'] = exp1 - exp2
    tickerdf['Signal'] = tickerdf['MACD'].ewm(span=9, adjust=False).mean()

    # plot
    st.write('***Closing price***')
    st.line_chart(tickerdf['Close'])

    st.write('***Volume***')
    st.line_chart(tickerdf['Volume'])

    st.write('***Moving Average & Exponential Moving Average***')
    df1 = tickerdf[['MA10', 'EMA10', 'Close']]
    st.line_chart(df1)


def oscilator(ticker):
    start1 = dt.datetime(2020, 1, 1)
    end1 = dt.datetime(2021, 5, 1)
    data = pdr.get_data_yahoo(ticker, start1, end1)

    high14 = data['High'].rolling(14).max()
    low14 = data['Low'].rolling(14).min()
    data['%K'] = (data['Close'] - low14) * 100 / (high14 - low14)
    data['%D'] = data['%K'].rolling(3).mean()
    data['upper'] = 80
    data['lower'] = 20
    data1 = data[['%K', '%D', 'Close', 'upper', 'lower']]
    st.write('***Stochastic Oscillator***')
    st.line_chart(data1)

# run the app using $streamlit run "<app_name>.py"
