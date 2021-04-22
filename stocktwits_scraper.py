import streamlit as st
import requests
import japanese_candlestick as candle


def stocktwits_feed(ticker):
    # candlestick chart
    candle.candlestick(ticker)
    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json")
    stocktwits_data = r.json()
    for message in stocktwits_data['messages']:
        # st.write(stocktwits_data)
        st.image(message['user']['avatar_url'])
        st.write(message['user']['username'])
        st.write(message['body'])
        st.write(message['created_at'])
