
from kafka import KafkaProducer
from json import dumps
from time import sleep
from datetime import datetime

import sys

BSS   = sys.argv[1]
TOPIC = sys.argv[2]

start=1000

def serialize(m) :
    return dumps(m).encode('utf-8')

producer = KafkaProducer( value_serializer=serialize , bootstrap_servers=[ BSS ]  )


for e in range(1000000):

    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    ts = datetime.timestamp(dt)

    data = { 'ts' : ts , 'value' : f"message for value {e} - {e + start}" }
    producer.send( TOPIC , value=data , key = b"partnkey" )
    print ( f"BSS = {BSS} TOPIC = {TOPIC} , Data={data}" )
    sleep(1)

print ("Exitting") 
sys.exit(0)
