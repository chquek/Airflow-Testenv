from kafka import KafkaConsumer , TopicPartition
from json import loads
import sys

TOPIC = sys.argv[1]
GROUP = sys.argv[2]

consumer = KafkaConsumer(
    TOPIC ,
    group_id=GROUP ,
    auto_offset_reset='latest',
    enable_auto_commit=True,
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['kafka:9092'] )

print ( f"TOPIC = {TOPIC} , GROUP = {GROUP} , consumer = ", dir(consumer) )
print ("\n\n")

PARTITIONS = []
for partition in consumer.partitions_for_topic(TOPIC):
    PARTITIONS.append(TopicPartition(TOPIC, partition))
    partn = TopicPartition(TOPIC,partition)
    print ( f"PARTN = {partn} , Committed = {consumer.committed( partn )}"  )

print ( "Begin Offsets " , consumer.beginning_offsets( PARTITIONS ) )
print ( "End   Offsets " , consumer.end_offsets( PARTITIONS ) )

print ("\n")

