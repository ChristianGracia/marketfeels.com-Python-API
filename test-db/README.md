# Test PostgreSQL DB

in this folder

`docker-compose up -d`

inject sql file with

`cat commands.sql | docker exec -i testdb_postgres psql -U user -d test_data`
