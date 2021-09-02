from kafka import KafkaProducer
from time import sleep
import os
import json
import transactions

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1/TRANSACTIONS_PER_SECOND

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers = KAFKA_BROKER_URL,
                             api_version=(0,11,5), 
                             value_serializer = lambda value: json.dumps(value).encode())
    
    print("Kafka producer is created")
    
    while True:
        transaction: dict = transactions.create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value = transaction)
        #print(transaction)
        sleep(SLEEP_TIME)



