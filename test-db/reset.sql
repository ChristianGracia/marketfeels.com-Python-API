DROP TABLE posts;

CREATE TABLE posts (
	id serial PRIMARY KEY,
	title VARCHAR ( 150 ) NOT NULL,
	subreddit VARCHAR ( 100 ) NOT NULL,
	post_description VARCHAR ( 1000 ) NOT NULL,
	reddit_id VARCHAR ( 60 ) UNIQUE NOT NULL,
	created_utc TIMESTAMP NOT NULL,
	author VARCHAR ( 60 ) NOT NULL,
	insert_timestamp TIMESTAMP NOT NULL
);
