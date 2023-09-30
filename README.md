

#  Setting up the Test Env

This repo is to suppose to go hand in hand with [Airflow-UI](https://github.com/chquek/Airflow-UI).

## Set up

- apt update
- apt install docker -y
- apt install docker-compose -y
- docker network create kinisi-net ( this step is necessary because the test environment and UI s on the same cluster )

## Usage

docker-compose up -d

This may take a while.  DB2 takes quite some time to initialise. 


## Monitor

Test if data sources is ready for use with the following commands :

DataSource | Command | Comment
--- | --- | --- |
DB2 | docker exec airflow-testenv_db2_1 su - db2inst1 -c "db2 connect to sample ; db2 'select * from employee'" |
MySQL non-ssl | docker exec -it airflow-testenv_mysql_nossl_1 bash -c "echo 'select * from movies' \| mysql -u root -pmysqlinst sandy" |
MySQL ssl | docker exec -it airflow-testenv_mysql_ssl_1 bash -c "echo 'select * from movies' \| mysql -u root -pmysqlinst sandy" |
REST server | docker exec -it airflow-testenv_mysql_nossl_1 bash -c "curl http://http:7654/dummy" |
Postgres | docker exec airflow-ui_postgres_1 bash -c "echo '\l' \| psql -U airflow -d airflow" | requires Airflow-UI to be running 

When the docker exec returns rows - this mean the datasource is ready.

## Monitor DB2

DB2 takes a much longer time to initialise.  Use this command to examine the logs :  docker-compose logs -f db2

DB2 is ready when the log shows following :

```
db2_1          | drop table cars
db2_1          | DB21034E  The command was processed as an SQL statement because it was not a
db2_1          | valid Command Line Processor command.  During SQL processing it returned:
db2_1          | SQL0204N  "DB2INST1.CARS" is an undefined name.  SQLSTATE=42704
db2_1          |
db2_1          | CREATE TABLE CARS ( id integer not null GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1) , make     char(20) , model    char(20) , year     int , price    decimal(7,2) )
db2_1          | DB20000I  The SQL command completed successfully.
...
...
...
db2_1          | EDUID   : 24                   EDUNAME: db2agent (idle) 0
db2_1          | FUNCTION: DB2 UDB, base sys utilities, sqeLocalDatabase::FreeResourcesOnDBShutdown, probe:16972
db2_1          | STOP    : DATABASE: SAMPLE   : DEACTIVATED: NO
```
