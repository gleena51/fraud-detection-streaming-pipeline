from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transactions = [
    {"id": 1, "user": "Alice", "amount": 120.5},
    {"id": 2, "user": "Bob", "amount": 850.0},
    {"id": 3, "user": "Charlie", "amount": 950.0},
    {"id": 4, "user": "Dave", "amount": 450.0},
    {"id": 5, "user": "Eve", "amount": 1500.0},
]

while True:
    transaction = random.choice(transactions)
    producer.send('transactions', transaction)
    print(f"Sent transaction: {transaction}")
    time.sleep(2)
