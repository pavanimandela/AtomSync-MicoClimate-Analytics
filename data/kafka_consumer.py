from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='atmosync-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("AtmoSync Kafka Consumer Started!")

try:
    for message in consumer:
        print("Received:", message.value)

except KeyboardInterrupt:
    print("\nConsumer stopped.")

finally:
    consumer.close()