from flask import Flask, json
from dotenv import load_dotenv
from services.reddit_service import reddit_api  
import psycopg2
from psycopg2 import Error
import os


load_dotenv() 

app = Flask(__name__)
app.register_blueprint(reddit_api, url_prefix='/reddit')

def db_init():
    try:
        connection = psycopg2.connect(
            user=os.getenv('postgres_user'),
            password=os.getenv('postgres_password'),
            host="localhost",
            port="5432",
            database=os.getenv('postgres_db'))

        cursor = connection.cursor()

        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection Sucessful and is now closed")

db_init()

print("connected to the db!")

@app.route('/')
def temp_route():
    return 'coming soon!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
    
