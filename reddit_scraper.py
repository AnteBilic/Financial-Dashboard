import praw
import streamlit as st

reddit_client_id = '4kbebt1oN5Jolw'
reddit_client_secret = 'Wgh0GLfh0-HWY-Nagpfir27IzgNR7A'
reddit_user_agent = 'Streamlit'

reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)


def redditor(cancer):
    subreddit = reddit.subreddit(cancer)

    for submission in subreddit.rising(limit=25):
        st.write(submission.author)
        st.write(submission.title)
        st.write(submission.url)
        st.write(submission.score)
        # st.write(submission.id)
