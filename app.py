from flask import Flask, json
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

    hot_posts = reddit.subreddit('wallstreetbets').new(limit=20) 

    lists = []
    for post in hot_posts:
        mini_list = []
        mini_list.append("title: " + post.title)
        mini_list.append("description: " + post.selftext)
        #mini_list.append("comment: " + post.comments)
        #mini_list.append("likes: " + post.likes)
        #mini_list.append("category: " + post.category)
        #mini_list.append("viewcount: " + post.view_count)
        mini_list.append("score: " + str(post.score))
        if post.selftext_html is not None:
            mini_list.append("selftext_html: " + post.selftext_html)
        mini_list.append("id: " + post.id)
        mini_list.append("created_utc: " + str(post.created_utc))
        #mini_list.append("discussion_type: " + post.discussion_type)
        #mini_list.append("author: " + post.author)
        
        lists.append(mini_list)
        print(dir(post))

    return_string = ""

    for list in lists:
        return_string += "[" + ", ".join(list) + "]"
    return return_string

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
