import pandas as pd

df = pd.read_csv("data/silver/silver_rides.csv")

daily_rides = (df.groupby("pickup_date").size().reset_index(name="total_rides"))

hourly_rides = (df.groupby("pickup_hour").size().reset_index(name="total_rides"))

weekday_rides = (df.groupby("pickup_weekday").size().reset_index(name="total_rides"))

base_rides = ( df.groupby("base").size() .reset_index(name="total_rides").sort_values("total_rides", ascending=False))

daily_rides.to_csv("data/gold/daily_rides.csv",index=False)

hourly_rides.to_csv("data/gold/hourly_rides.csv",index=False)

weekday_rides.to_csv("data/gold/weekday_rides.csv",index=False)

base_rides.to_csv("data/gold/base_rides.csv",index=False)

print("Gold Layer Created Successfully")