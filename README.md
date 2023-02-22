# housing
start
- docker-compose build --no-cache
- docker-compose up


dump data to docker postgresql container 

docker exec -i {db container name} /bin/bash -c "PGPASSWORD={POSTGRES_PASSWORD} psql --username {POSTGRES_USER} {POSTGRES_DB}" < ./{YOUR DATA}.sql