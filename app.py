from flask import Flask, json
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from services.reddit_service import reddit_api  


load_dotenv() 

app = Flask(__name__)
app.register_blueprint(reddit_api, url_prefix='/reddit') 

engine = create_engine("postgresql://user:password@localhost:5432/test-db")
db = scoped_session(sessionmaker(bind=engine))

print("connected to the db!")

@app.route('/')
def temp_route():
    return 'coming soon!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
