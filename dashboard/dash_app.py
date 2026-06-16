import pandas as pd
from pathlib import Path
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import plotly.express as px

st.set_page_config(page_title="Uber Ride Dashboard",page_icon="taxi",layout="wide")
st_autorefresh(interval=10000, key="refresh")

BASE_DIR = Path(__file__).resolve().parent.parent


daily_df = pd.read_csv(BASE_DIR / "data" / "gold" / "daily_rides.csv")
hourly_df = pd.read_csv(BASE_DIR / "data" / "gold" / "hourly_rides.csv")
weekday_df = pd.read_csv(BASE_DIR / "data" / "gold" / "weekday_rides.csv")


base_df = pd.read_csv(BASE_DIR / "data" / "gold" / "base_rides.csv")
silver_df = pd.read_csv(BASE_DIR / "data" / "silver" / "silver_rides.csv")
silver_df["pickup_datetime"] = pd.to_datetime(silver_df["pickup_datetime"])

total_rides = len(silver_df)

latest_time = silver_df["pickup_datetime"].max()

new_rides = len(silver_df[silver_df["pickup_datetime"] >= latest_time - pd.Timedelta(minutes=1)])

active_bases = silver_df["base"].nunique()

latest_ride_time = latest_time.strftime("%Y-%m-%d %H:%M:%S")

rides_per_minute = (silver_df.set_index("pickup_datetime").resample("1min").size().reset_index(name="total_rides"))

rides_per_minute = rides_per_minute.tail(30)

st.title("Uber Ride Dashboard")


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Rides",f"{total_rides:,}")
col2.metric("New Rides (Last 1 Min)",f"{new_rides:,}")
col3.metric("Active Bases",f"{active_bases:,}")
col4.metric("Latest Ride Time",latest_ride_time)


fig_realtime = px.line(
    rides_per_minute,
    x="pickup_datetime",
    y="total_rides",
    title="Real-Time Ride Volume (Last 30 Minutes)"
)

st.plotly_chart(fig_realtime,use_container_width=True)

fig_daily = px.line(
    daily_df,
    x="pickup_date",
    y="total_rides",
    title="Daily Ride Trend"
)

fig_hourly = px.bar(
    hourly_df,
    x="pickup_hour",
    y="total_rides",
    title="Peak Pickup Hours"
)

fig_weekday = px.pie(
    weekday_df,
    names="pickup_weekday",
    values="total_rides",
    hole=0.5,
    title="Weekday Ride Distribution"
)

fig_base = px.bar(
    base_df,
    x="base",
    y="total_rides",
    title="Top Uber Bases"
)

left_col, right_col = st.columns(2)

with left_col:

    st.plotly_chart(fig_daily,use_container_width=True)

    st.plotly_chart(fig_weekday,use_container_width=True)

with right_col:

    st.plotly_chart(fig_hourly,use_container_width=True)

    st.plotly_chart(fig_base,use_container_width=True)