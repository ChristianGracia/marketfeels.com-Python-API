CREATE TABLE posts (
	id serial PRIMARY KEY,
	title VARCHAR ( 50 ) UNIQUE NOT NULL,
	subreddit VARCHAR ( 50 ) NOT NULL,
	post_description VARCHAR ( 1000 ) NOT NULL,
	reddit_id VARCHAR ( 60 ) UNIQUE NOT NULL,
	created_utc TIMESTAMP NOT NULL,
	author VARCHAR ( 40 ) UNIQUE NOT NULL
);

INSERT INTO posts (title, subreddit, post_description, reddit_id, created_utc, author)
VALUES ('Cardinal', 'Pennystocks', 'dededededededede 21', '2121212', '2020-01-01 10:10:10+05:30', 'cg');

select * from posts;