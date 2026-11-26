import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'sensor-data'

print("AtmoSync Kafka Producer Started!")

try:
    while True:
        sensor_data = {
            "container_id": "CONT-001",
            "timestamp": datetime.now().isoformat(),
            "temperature": round(random.uniform(2, 12), 2),
            "humidity": round(random.uniform(60, 95), 2),
            "vibration": round(random.uniform(0.1, 2.0), 2),
            "commodity": "Avocado"
        }

        producer.send(topic, sensor_data)
        producer.flush()

        print("Sent:", sensor_data)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nProducer stopped.")

finally:
    producer.close()