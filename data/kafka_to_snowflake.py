import json
import csv
import os
from kafka import KafkaConsumer

os.makedirs("data/processed", exist_ok=True)

consumer = KafkaConsumer(
    "sensor-data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    group_id="atmosync-csv-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

file_path = "data/processed/live_sensor_data.csv"

print("AtmoSync Live Data Collection Started!")

try:
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                "container_id", "timestamp", "temperature",
                "humidity", "vibration", "commodity"
            ])

        for message in consumer:
            data = message.value
            writer.writerow([
                data["container_id"],
                data["timestamp"],
                data["temperature"],
                data["humidity"],
                data["vibration"],
                data["commodity"]
            ])
            file.flush()
            print("Saved:", data)

except KeyboardInterrupt:
    print("Data collection stopped.")

finally:
    consumer.close()