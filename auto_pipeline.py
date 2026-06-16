import time
import subprocess

while True:

    subprocess.run(["python", "silver_transform.py"])

    subprocess.run(["python", "gold_transform.py"])

    print("Pipeline Refreshed")

    time.sleep(5)