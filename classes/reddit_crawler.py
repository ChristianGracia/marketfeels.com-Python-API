import praw
import os
from classes.db_client import DbClient

class RedditCrawler():
    crawler = None

    def __init__(self, client_id, client_secret, user_agent):
        self.crawler = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent)

    def get_crawler(self): 
        return self.crawler

    def stream_subreddits(self, subreddits):

        client = DbClient(os.getenv('postgres_user'), os.getenv('postgres_password'), os.getenv('postgres_path'), os.getenv('postgres_port'), os.getenv('postgres_db'))

        print("Searching reddit for these " + subreddits.replace("+", " "))

        stream = self.crawler.subreddit(subreddits).stream.submissions()
        for submission in stream:
            client.insert_reddit_submission(
                title=submission.title, post_description=submission.description, 
                subreddit=submission.subreddit, id=submission.id, created_utc=submission.created_utc,
                author=submission.author
                )

            # print("title: " + submission.title)
            # print("subreddit: " + str(submission.subreddit))
            # print("description: " + post.selftext)
            # print("comment: " + post.comments)
            #     print("likes: " + post.likes)
            #     print("category: " + post.category)
            #     print("viewcount: " + post.view_count)
            #     print("score: " + str(post.score))
            #     if post.selftext_html is not None:
            #         print("selftext_html: " + post.selftext_html)
            #     print("id: " + post.id)
            #     print("created_utc: " + str(post.created_utc))
            #     print("discussion_type: " + post.discussion_type)
            #     print("author: " + post.author)