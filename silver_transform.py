import pandas as pd

# Read Bronze Layer
df = pd.read_csv("data/bronze/bronze_rides.csv")

# Remove duplicates
df = df.drop_duplicates()

# Convert datetime
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])

# Create new columns
df["pickup_date"] = df["pickup_datetime"].dt.date

df["pickup_hour"] = df["pickup_datetime"].dt.hour

df["pickup_weekday"] = df["pickup_datetime"].dt.day_name()

# Save Silver Layer
df.to_csv("data/silver/silver_rides.csv",index=False)

print("Silver Layer Created Successfully!")
print(f"Rows Processed: {len(df)}")