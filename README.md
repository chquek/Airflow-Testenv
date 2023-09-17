


#  Setting up the Test Env


Repo : http://shiga:3000/quekch/Kinisi-TestEnv.git

Development :

- carmen /test/env:/Kinisi-TestEnv
- cd /testenv/Kinisi-Testenv/DB2
- tar cvf data.tar data
- gzip data.tar
- scp data.tar.gz root@cuclone.kinisi.biz:/root/Kinisi-TestEnv/DB2

Production :

- cuclone /root/Kinisi-TestEnv
- tar cvf DB2/data folder and import it here.
- docker-compose -f docker-compose.clone.yaml up


This step is to avoid re-generating certificates and have to amend the datasource
