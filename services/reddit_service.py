from flask import Blueprint
from flask import Flask, abort, request, jsonify  
import json  
from flask import jsonify
from classes.reddit_crawler import RedditCrawler


import os

from dotenv import load_dotenv

reddit_api = Blueprint('reddit_api', __name__)  

@reddit_api.route('/posts') 
def get_posts():
    
    reddit_crawler = RedditCrawler(os.getenv('client_id'), os.getenv('client_secret'), os.getenv('user_agent'))
    
    #submissions = reddit_crawler.subreddit('wallstreetbets').new(limit=20) 

    submissions = reddit_crawler.stream_subreddits(os.getenv('subreddits'))
    
    return "return_string"


class JSONObject:  
  def __init__( self, dict ):  
      vars(self).update( dict )