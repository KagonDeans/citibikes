import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

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

#grouping by day of the week and suming the number of trips.
daily_trips = cb.groupby('day_of_week')['num_of_trips'].sum().reset_index()

# Plotting 
fig = px.bar(daily_trips, x='day_of_week', y='num_of_trips', 
             title='Total Number of Trips per Day of the Week', 
             labels={'day_of_week': 'Day of the Week', 'num_of_trips': 'Total Number of Trips'})

# showing
st.plotly_chart(fig)

st.write("")
st.write("")
st.write("")

# grouping by season and suming the num of trips.
seasonal_trips = cb.groupby('season')['num_of_trips'].sum().reset_index()

# Plotting
fig = px.pie(seasonal_trips, values='num_of_trips', names='season', title='Number of Trips by Season')
fig.update_layout(width=800, height=600)
# showing
st.plotly_chart(fig)
























































