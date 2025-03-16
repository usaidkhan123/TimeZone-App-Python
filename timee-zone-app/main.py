import streamlit as st
from datetime import datetime        
from zoneinfo import ZoneInfo       # it provide timezone information

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
   "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["Asia/Karachi"])

st.subheader("Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")      # strftime is used to convert datetime object into string formatt
    st.write(f"{tz}:{current_time }") 


st.subheader("Convert Time Between Timezones")
current_time = st.time_input("Curruent Time", value=datetime.now().time())          # time_input values of time on ui 
from_tz = st.selectbox("From Timezone", TIME_ZONES,index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES,index=1)

if st.button("Convert Time"):
    dt  = datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_tz))       # day , time , from_tz ki timezone
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")     # astimezone is used to convert time from one timezone to another
    st.success(f"Converted Time: {converted_time}")










