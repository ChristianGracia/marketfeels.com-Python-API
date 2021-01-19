import psycopg2
from psycopg2 import Error

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
            
        except (Exception, Error) as error:
            print("Error while instantiating PostgreSQL class instance", error)

    def insert_reddit_submission(self, title, post_description, subreddit, reddit_id, created_utc, author):

        cursor = self.db_connection.cursor()

        cursor.execute("""
        INSERT INTO posts (title, subreddit, post_description, reddit_id, created_utc, author)
        VALUES (%s, %s, %s, %s, %s, %s);
        """,
        ('Cardinal', 'Pennystocks', 'dededededededede 21', '2121212', '2020-01-01 10:10:10+05:30', 'cg');)

        

    def log_databse_details(self):

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



