

#  Setting up the Test Env

This repo is to suppose to go hand in hand with [Airflow-UI](https://github.com/chquek/Airflow-UI).


## Run

docker-compose up -d

This may take a while.  DB2 takes quite a while to initialise. 

Test if data sources is ready for use with the following commands :

DataSource | Command | Comment
--- | --- | --- |
DB2 | docker exec airflow-testenv_db2_1 su - db2inst1 -c "db2 connect to sample ; db2 'select * from employee'" |
MySQL non-ssl | docker exec -it airflow-testenv_mysql_nossl_1 bash -c "echo 'select * from movies' \| mysql -u root -pmysqlinst sandy" |
MySQL ssl | docker exec -it airflow-testenv_mysql_ssl_1 bash -c "echo 'select * from movies' \| mysql -u root -pmysqlinst sandy" |
Postgres | docker exec airflow-ui_postgres_1 bash -c "echo '\l' \| psql -U airflow -d airflow" | requires Airflow-UI to be running 
