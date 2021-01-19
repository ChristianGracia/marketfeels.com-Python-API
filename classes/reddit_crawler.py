import praw

class RedditCrawler():
    crawler = None

    def __init__(self, client_id, client_secret, user_agent):
        self.crawler = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = user_agent)

    def get_crawler(self): 
        return self.crawler

    def stream_subreddits(self, subreddits):
        print(subreddits)
        stream = self.crawler.subreddit(subreddits).stream.submissions()
        for submission in stream:
           print("title: " + submission.title)
           print("title: " + str(submission.subreddit))