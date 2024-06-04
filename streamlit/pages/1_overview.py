import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cb = pd.read_csv("../data/cb_stream.csv")


# #st.image("../photos/Total_trips.png")

st.title('Bike Byte 🚲')

st.write("")
st.write("")
st.write("")

st.markdown("""Hi everyone, let's break down the citibike data. 
         In total there were **67,720,005** bikes rides. There were **20,551,697** in 2019,
        **19,506,857** in 2020, & **27,661,451** in 2021. """)

st.write("")
st.markdown("""The average trip duration across all years is **1110.5 seconds or 18.5 minutes** The average median trip duration is **673 seconds or 11 minutes**
""")
st.write("")
st.write("")

daily_trips = cb.groupby('day_of_week')['num_of_trips'].sum()

fig, ax = plt.subplots()
ax.bar(daily_trips.index, daily_trips)

ax.set_title('Total Number of Trips per Day of the Week')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Total Number of Trips')
ax.set_xticks(range(7))
ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], rotation=0)

st.pyplot(fig)

st.write("")
st.write("")
st.write("")

seasonal_trips = cb.groupby('season')['num_of_trips'].sum()

fig, ax = plt.subplots()
ax.pie(seasonal_trips, labels=seasonal_trips.index, autopct='%1.1f%%')

ax.set_title('Number of Trips by Season')
plt.legend(title = "Seasons:")

st.pyplot(fig)



































































