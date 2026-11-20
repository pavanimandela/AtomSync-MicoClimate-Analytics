import csv
import random
import os
from datetime import datetime, timedelta

# Create data folder
os.makedirs("data", exist_ok=True)

# CSV file location
file_path = "data/sensor_data.csv"

# Dataset columns
columns = [
    "container_id",
    "timestamp",
    "temperature",
    "humidity",
    "vibration",
    "commodity"
]

# Generate sample sensor data
start_time = datetime.now()

with open(file_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    for container in range(1, 4):
        for reading in range(20):
            writer.writerow({
                "container_id": f"C00{container}",
                "timestamp": (
                    start_time + timedelta(minutes=reading * 5)
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": round(random.uniform(2, 12), 2),
                "humidity": round(random.uniform(60, 95), 2),
                "vibration": round(random.uniform(0.1, 2.0), 2),
                "commodity": "Avocado"
            })

print("Dataset created successfully!")
print("Total records: 60")
print("File location:", file_path)