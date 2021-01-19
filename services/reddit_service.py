from flask import Blueprint
import json  
import os
from dotenv import load_dotenv

from classes.reddit_crawler import RedditCrawler

reddit_api = Blueprint('reddit_api', __name__)  

@reddit_api.route('/posts') 
def get_posts():
    
    reddit_crawler = RedditCrawler(os.getenv('client_id'), os.getenv('client_secret'), os.getenv('user_agent'))

    submissions = reddit_crawler.stream_subreddits(os.getenv('subreddits'))
    
    return "stream running"


class JSONObject:  
  def __init__( self, dict ):  
      vars(self).update( dict )