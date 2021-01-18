CREATE TABLE posts (
	id_num serial PRIMARY KEY,
	post_name VARCHAR ( 50 ) UNIQUE NOT NULL,
	post_details VARCHAR ( 1000 ) NOT NULL,
	post_id VARCHAR ( 70 ) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL
);

INSERT INTO posts (post_name, post_details, post_id, created_on)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', '2020-01-01 10:10:10+05:30');

select * from posts;