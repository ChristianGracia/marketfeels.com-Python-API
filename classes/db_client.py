import psycopg2
from psycopg2 import Error
from datetime import datetime
import time 

class DbClient():

    db_connection = None

    def __init__(self, user, password, host, port, database):
        try:
            self.db_connection = psycopg2.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database)
            print("connected to db!")
            
        except (Exception, Error) as error:
            print("Error while instantiating PostgreSQL class instance", error)

    def insert_reddit_submission(self, title, post_description, subreddit, reddit_id, created_utc, author, post_url):

        cursor = self.db_connection.cursor()

        if not self.check_if_post_in_db(cursor, reddit_id):
  
            SQL = 'INSERT INTO posts (title, subreddit, post_description, reddit_id, created_utc, author, post_url, insert_timestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'
            data = (title[:150], subreddit, post_description[:997] + "...", reddit_id, datetime.utcfromtimestamp(created_utc), str(author)[:40], post_url, datetime.utcfromtimestamp(time.time()))  
            cursor.execute(SQL, data)
            self.db_connection.commit()
            print("submission successful")
        else:
            print("Post found but it was already in the database.")

        cursor.close()
        
    def check_if_post_in_db(self, cursor, reddit_id):

        cursor.execute("SELECT reddit_id FROM posts WHERE reddit_id = %s", (reddit_id,))
        return cursor.fetchone() is not None

    def log_database_details(self):

        try:
            cursor = self.db_connection.cursor()
            print("PostgreSQL server information")
            print(self.db_connection.get_dsn_parameters(), "\n")

            cursor.execute("SELECT version();")

            record = cursor.fetchone()

            print("You are connected to - ", record, "\n")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (self.db_connection):

                cursor.close()
                self.db_connection.close()

                print("PostgreSQL connection Sucessful and is now closed")



