import tweepy
import streamlit as st

# authenticating twitter api credentials
consumer_key = 'Gn4qWWHQPh3fzKn9RM40xl83B'
consumer_secret = 'EK4mMHsP2aZwt7jb4qFCGJhMnl1SIT5O3tSY5NLZSjeH9mrlGU'
access_token = '811640118-xbYVJbn6RC7BlqW6OIjbp26wIdIdLoJQfRqbWBCZ'
access_token_secret = 'vWNa3DGmACZTMl3imOOIIDrM11YGsK9Kn7ot5vzZtNIST'


# instantiating the api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# creating api object
api = tweepy.API(auth)

twitter_usernames = [
    'jimcramer',
    'traderstewie',
    'the_chart_life',
    'canuck2usa',
    'sunrisetrader',
    'tmltrader',
    'ritzholtz',
    'elerianm',
    'PeterLBrandt',
    'ZeroHedge',
    'TheStalwart',
    'paulkrugman',
    'steve_hanke'
]


def get_tweets():
    for username in twitter_usernames:
        user = api.get_user(username)
        tweets = api.user_timeline(username)

        st.image(user.profile_image_url)
        st.subheader(username)

        for tweet in tweets:
            if '$' not in tweet.text:
                continue
            else:
                words = tweet.text.split(' ')
                for word in words:
                    if word.startswith('$') and word[1:].isalpha():
                        symbol = word[1:]
                        st.write(symbol)
                        st.write(tweet.text)
                        st.image(f"https://finviz.com/chart.ashx?t={symbol}")
