from flask import Flask, json
from dotenv import load_dotenv

import os

from services.reddit_service import reddit_api
from classes.db_client import DbClient

load_dotenv() 

app = Flask(__name__)
app.register_blueprint(reddit_api, url_prefix='/reddit')

def db_init():
    client = DbClient(os.getenv('postgres_user'), os.getenv('postgres_password'), os.getenv('postgres_path'), os.getenv('postgres_port'), os.getenv('postgres_db'))
    client.log_database_details()

db_init()

@app.route('/')
def main():
    return 'Marketfeels.com Python API'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
    
