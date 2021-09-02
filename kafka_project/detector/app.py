from kafka import KafkaConsumer, KafkaProducer
import json
import os

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
LEGIT_TOPIC = os.environ.get("LEGIT_TOPIC")
FRAUD_TOPIC = os.environ.get("FRAUD_TOPIC")

def is_suspicious(transaction: dict) -> bool:
    """Determine whether transaction is considered suspicious based on an amount greater than or equal to $900"""
    return transaction["amount"] >= 900

if __name__ == "__main__":
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers = KAFKA_BROKER_URL,
        value_deserializer = json.loads,
    )
    
    producer = KafkaProducer(
        bootstrap_servers = KAFKA_BROKER_URL,
        api_version=(0,11,5),
        value_serializer = lambda value: json.dumps(value).encode()
        )


    for message in consumer:
        transaction:dict = message.value
        topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
        producer.send(topic, value=transaction)
        #print(topic, transaction)





