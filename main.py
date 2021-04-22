import streamlit as st
import charting as chart
import twitter as twt
import japanese_candlestick as candle
import cryptodash as cry
import reddit_scraper as rdt
import stocktwits_scraper as stocktwits

st.set_page_config(layout="wide")  # st.beta_set_page_config(layout="wide")

option = st.sidebar.selectbox("Which dashboard", ('Cyptocurrency overview', 'Reddit', 'Stocktwits', 'Twitter',
                                                  'Chart', 'Candlestick chart',))

# CRYPTO
if option == 'Cyptocurrency overview':
    st.title(option)
    #    twt.get_tweets()
    cry.crpyto_dash()


if option == 'Candlestick chart':
    st.title(option)
    ticker = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)
    candle.candlestick(ticker)


if option == 'Stocktwits':
    st.title('Stocktwits shits and giggles')
    st.image('https://financialit.net/sites/default/files/stocktwits.png')
    ticker = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)
    stocktwits.stocktwits_feed(ticker)


if option == 'Reddit':
    cancer = st.sidebar.selectbox("Which subreddit?", ('wallstreetbets', 'Superstonk', 'GME', 'stocks', 'investing',
                                                       'finance', 'StockMarket'))
    # sort = st.sidebar.selectbox("Filter", ('top', 'new', 'controversial', 'hot', 'rising', 'gilded'))
    st.title('Pure fucking cancer')
    st.image('https://www.motivproductions.co.uk/wp-content/uploads/2014/10/Reddit-Header.jpg')
    # st.image('https://static.media.thinknum.com/media/uploads/blog/image-fullwidth/.thumbnails/alternativedata_wall_street_bets_full_width.jpg/alternativedata_wall_street_bets_full_width-1200x400.jpg')
    rdt.redditor(cancer)


# Basic charts... For now
if option == 'Chart':
    ticker = st.sidebar.text_input("Symbol", value='AAPL', max_chars=5)
    chart.oscilator(ticker)
    chart.charting(ticker)
    candle.show_df(ticker)


# tweet streaming dash
if option == 'Twitter':
    st.image('https://business.twitter.com/content/dam/business-twitter/help/header/header2.png.twimg.1920.png')
    twt.get_tweets()
