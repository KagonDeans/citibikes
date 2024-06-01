import streamlit as st
import pandas as pd

st.title("How Many trips")

st.write("### Input Data")
col1, col2 = st.columns(2)
day_of_week = col1.text_input("Day of the Week")
season = col1.text_input("Season")
maxium_temp = col1.number_input("Max Temp (in F°)", min_value = 15, value = 98)

st.write("### Num of Trips")
col1 = st.columns(1)
col1.metric(label = "Number of predicted trips")
