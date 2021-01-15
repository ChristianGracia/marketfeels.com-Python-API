from flask import Flask
from dotenv import load_dotenv

import praw
import os

load_dotenv() 

app = Flask(__name__)

@app.route('/')
def temp_route():
    return 'coming soon!'

@app.route('/posts')
def get_posts():
    reddit = praw.Reddit(client_id = os.getenv('client_id'), client_secret = os.getenv('client_secret'), user_agent = os.getenv('user_agent'))

    hot_posts = reddit.subreddit('MachineLearning').hot(limit=10) 

    list = []
    for post in hot_posts:
        print(post.title)

    return 'coming soon!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
