
# Intro

This is a self contained test environment for a Kafka environment.   It uses files from the following git to create my test image.

- https://github.com/wurstmeister/kafka-docker.git.


## Usage

CMD="docker exec -it kafka_python_1 python3" .  Need the -it option.  Otherwise when use ctrl-c , the program will still run in the background.

Command | Description
--- | --- |
docker-compose up | to bring up the Kafka server , zookeeper , and Python environment
$CMD py/producer.py test-topic | start writing messages to this topic
$CMD py/examine.py test-topic user1 | examine the topic length and offets as user1
$CMD py/consumer.py test-topic user1 | consume messages in test-topic as user1


## terms

Consumer :

earliest :  start reading from 1st message
latest : start reading from end of queue
