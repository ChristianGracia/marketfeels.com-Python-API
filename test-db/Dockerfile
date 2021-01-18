FROM postgres:12
COPY sql/*.sql /docker-entrypoint-initdb.d/
RUN psql -h psql_postgis_db -U gis_admin gis