import pandas_datareader as pdr
import datetime as dt
import plotly.graph_objects as go
import streamlit as st


def candlestick(ticker):
    start = dt.datetime(2015, 1, 1)
    end = dt.datetime(2021, 5, 1)
    df = pdr.get_data_yahoo(ticker, start, end)

    # with rangeslider
    # st.subheader('With rangeslider')
    fig = go.Figure(data=[go.Candlestick(x=df.index.get_level_values('Date'),
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    # st.plotly_chart(fig, use_container_width=True)

    # without rangeslider
    # st.subheader('Without rangeslider')
    st.subheader(f'{ticker} closing price')
    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)


def show_df(ticker):
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime(2021, 5, 1)
    df = pdr.get_data_yahoo(ticker, start, end)
    reversed_df = df.iloc[::-1]
    st.subheader(f'{ticker} dataframe')
    st.dataframe(reversed_df)
