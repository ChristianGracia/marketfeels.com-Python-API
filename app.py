from flask import Flask, json
from dotenv import load_dotenv
from services.reddit_service import reddit_api  
import psycopg2
from psycopg2 import Error
import os


load_dotenv() 

app = Flask(__name__)
app.register_blueprint(reddit_api, url_prefix='/reddit') 

print(os.getenv('postgres_user'))
print(os.getenv('postgres_password'))
print(os.getenv('postgres_db'))

connection = psycopg2.connect(
    user=os.getenv('postgres_user'),
    password=os.getenv('postgres_password'),
    host="localhost",
    port="5432",
    database=os.getenv('postgres_db'))

print("connected to the db!")

@app.route('/')
def temp_route():
    return 'coming soon!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
