import praw
import os
from classes.db_client import DbClient
import time

class RedditCrawler():
    crawler = None

    def __init__(self, client_id, client_secret, user_agent):
        self.crawler = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent)

    def get_crawler(self): 
        return self.crawler

    def stream_subreddits(self, subreddits):

        client = DbClient(os.getenv('postgres_user'), os.getenv('postgres_password'), os.getenv('postgres_path'), os.getenv('postgres_port'), os.getenv('postgres_db'))

        time.sleep(1)

        print("Searching reddit for these " + subreddits.replace("+", " "))

        stream = self.crawler.subreddit(subreddits).stream.submissions()
        for submission in stream:
            client.insert_reddit_submission(
                title=submission.title, post_description=submission.selftext, 
                subreddit=str(submission.subreddit), reddit_id=submission.id, created_utc=submission.created_utc,
                author=submission.author, post_url=submission.url
                )