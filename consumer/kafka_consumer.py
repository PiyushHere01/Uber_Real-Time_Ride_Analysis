from kafka import KafkaConsumer
from pathlib import Path

import json
import pandas as pd
import os

consumer = KafkaConsumer(
    'uber-rides',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)



BASE_DIR = Path(__file__).resolve().parent.parent

output_file = BASE_DIR / "data" / "bronze" / "bronze_rides.csv"

if not os.path.exists(output_file):

    df = pd.DataFrame(columns=[
        "ride_id",
        "pickup_datetime",
        "lat",
        "lon",
        "base"
    ])

    df.to_csv(output_file,index=False)


print("Consumer Started...")

for message in consumer:

    ride = message.value

    print(f"Received ---> {ride}")

    df = pd.DataFrame([ride])

    df.to_csv(output_file,mode='a',header=False,index=False)