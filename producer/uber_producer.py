from kafka import KafkaProducer
from datetime import datetime

import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

ride_id = 1

while True:

    ride_event = {
        "ride_id": ride_id,
        "pickup_datetime": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "lat": round(random.uniform(40.5, 41.0),6),
        "lon": round(random.uniform(-74.2, -73.7),6),
        "base": random.choice([
            "B02512",
            "B02598",
            "B02617",
            "B02682",
            "B02764"
        ])
    }

    producer.send("uber-rides",value=ride_event)

    print(f"Sent -> {ride_event}")

    ride_id += 1

    time.sleep(2)