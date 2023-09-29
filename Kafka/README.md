
# Intro

This is a self contained test environment for Kafka topics.   It uses files from the following git to create my test image.

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

- earliest :  start reading from 1st message
- latest : start reading from end of queue


## Use with Airflow

### connection id - kinisi-kafka
```
{
  "bootstrap.servers": "ubuntu:9092",
  "group.id": "aaa"
}
```

### DAG

Kafka.py to read/write


``` python
import json

def producer():
  print ("Producer called" )
  for i in range(20):
    yield (json.dumps( { 'k' : i }) , json.dumps( { 'v' : i + 1 } ))


# append the message to the data pointer
def consumer(message, prefix=None , dataptr=[] ):
  key = message.key().decode('utf-8')
  value = json.loads( message.value().decode('utf-8') )
  print (f"CONSUMER : {prefix} {message.topic()} @ {message.offset()}; {key} : {value}")
  dataptr.append(value)

```

### Tasks

create task to write to topic test-connection, and read from topic test-consumer.  In the host that is running the docker , run the following to keep writing rows to the topic :


- CMD="docker exec -it kafka_python_1 python3" 
- $CMD py/producer.py kafka test-consumer
