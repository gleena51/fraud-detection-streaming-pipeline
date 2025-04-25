# Fraud Detection Streaming Pipeline

This project demonstrates a real-time fraud detection streaming pipeline using Apache Flink, Kafka, and Python.

## Features

- Ingests real-time transaction data from Kafka.
- Detects fraudulent transactions based on a simple rule (e.g., amount > $900).
- Flags and prints suspicious transactions.
- Simulated Kafka producer to send fake transactions.

## Folder Structure

```
fraud-detection-streaming-pipeline/
├── README.md
├── requirements.txt
├── flink_job/
│   ├── fraud_detection.py
│   └── utils.py
├── kafka/
│   ├── sample_transactions.json
│   └── kafka_producer.py
```

## How to Run

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start a local Kafka broker (or connect to your cloud Kafka).

3. Run the Kafka producer to simulate transactions:
   ```bash
   python kafka/kafka_producer.py
   ```

4. Run the Flink fraud detection job:
   ```bash
   python flink_job/fraud_detection.py
   ```

## Notes

- This is a simple demo project. In production, use proper schema validation, secure Kafka brokers, and enhanced fraud detection models.
