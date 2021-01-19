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
        # for submission in stream:
        #    print("title: " + submission.title)
        #    print("title: " + str(submission.subreddit))

    
        #     print("description: " + post.selftext)
        #     print("comment: " + post.comments)
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