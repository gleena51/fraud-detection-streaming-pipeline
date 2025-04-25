from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
from pyflink.datastream.connectors import FlinkKafkaConsumer
import json
from flink_job.utils import parse_transaction

def detect_fraud(transaction):
    if transaction['amount'] > 900:
        return True
    return False

def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_stream_time_characteristic(TimeCharacteristic.ProcessingTime)

    kafka_props = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'fraud-detector',
        'key.deserializer': 'org.apache.kafka.common.serialization.StringDeserializer',
        'value.deserializer': 'org.apache.kafka.common.serialization.StringDeserializer',
    }

    consumer = FlinkKafkaConsumer(
        topics='transactions',
        deserialization_schema=lambda msg: msg.decode('utf-8'),
        properties=kafka_props
    )

    stream = env.add_source(consumer)
    parsed_stream = stream.map(parse_transaction)

    suspicious = parsed_stream.filter(detect_fraud)
    suspicious.print()

    env.execute("Fraud Detection Streaming Job")

if __name__ == '__main__':
    main()
