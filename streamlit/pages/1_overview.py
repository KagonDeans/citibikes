import streamlit as st
import pandas as pd
import plotly.express as px

cb = pd.read_csv("../data/citibike_vis.csv")

# Creating tabs
tab1, tab2, tab3 = st.tabs(["Trips", "Time", "Weather"])

# Tab 1: Trips
with tab1:
    st.title('Bike Byte 🚲')

    st.write("")
    st.write("")

    st.markdown("""Let's break down the citibike data. 
             In total there were **67,720,005** bike rides. There were **20,551,697** in 2019,
            **19,506,857** in 2020, & **27,661,451** in 2021. """)

    st.write("")
    st.write("")
    st.write("")

    # Days of week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Grouping by day of the week and summing the number of trips.
    daily_trips = cb.groupby('day_of_week')['num_of_trips'].sum().reset_index()

    # Plotting 
    fig = px.bar(daily_trips, x = 'day_of_week', y = 'num_of_trips', 
                    title = 'Total Number of Trips per Day of the Week', 
                    labels = {'day_of_week': 'Day of the Week', 'num_of_trips': 'Total Number of Trips'},
                    category_orders = {'day_of_week': days})

    # Update tick labels
    fig.update_layout(xaxis = {'tickvals':  daily_trips['day_of_week'], 'ticktext': days})
    
    # Showing
    st.plotly_chart(fig)
        
    st.write("")
    st.write("")
    st.write("")

    # Grouping by season and summing the number of trips.
    seasonal_trips = cb.groupby('season')['num_of_trips'].sum().reset_index()

    st.write("Below is a pie chart that shows the percentage of trips taken each season:")

    # Plotting
    fig = px.pie(seasonal_trips, values = 'num_of_trips', names = 'season', title = 'Number of Trips by Season')
    fig.update_layout(width = 800, height = 600)
    
    # Showing
    st.plotly_chart(fig)
        
    st.write("")
    st.write("")
    st.write("")
   
    # Grouping by year, month, season 
    mon_year_season = cb.groupby(['year', 'month', 'season'])['num_of_trips'].sum().reset_index()
    mon_year_season['month_year_season'] = mon_year_season['month'].astype(str) + ' ' + mon_year_season['year'].astype(str) + ' ' + mon_year_season['season']

    fig = px.line(mon_year_season, x = 'month_year_season', y = 'num_of_trips', 
                      title = 'Number of Trips by Month, Year and Season',
                      labels = {'month_year_season': 'Month, Year and Season', 'num_of_trips': 'Number of Trips'})

    fig.update_layout(width = 800, height = 600)
    fig.update_traces(mode = 'lines+markers')

    # Displaying 
    st.plotly_chart(fig)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Tab 2: Time
with tab2:
    st.title('Time')
    st.markdown("""
    - **The median trip duration is 11 minutes**
    - **Average trip duration: 18.5 minutes**
    """)
    # days of week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # Grouping by day of the week and calculating the median trip duration
    med_trip_duration = cb.groupby('day_of_week')['median_trip_duration'].median().reset_index()

    # Plotting
    fig = px.bar(med_trip_duration, x ='day_of_week', y = 'median_trip_duration', 
             title = 'Median Trip Duration per Day of the Week', 
             labels = {'day_of_week': 'Day of the Week', 'median_trip_duration': 'Median Trip Duration in seconds'},
             category_orders = {'day_of_week': days})

    # Update tick labels
    fig.update_layout(xaxis = {'tickvals': med_trip_duration['day_of_week'], 'ticktext': days})

    # Showing plot
    st.plotly_chart(fig)
    
    
    st.write("")
    st.write("")
    st.write("")
    
    # Grouping by season and obtaining median trip durations
    seasonal_trips = cb.groupby('season')['median_trip_duration'].median().reset_index()

    # Plotting a box plot
    fig = px.box(cb, x = 'season', y = 'median_trip_duration', title = 'Median Trip Durations by Season')
    fig.update_layout(width = 800, height = 600)

    # Showing the plot
    st.plotly_chart(fig)

    st.write("")
    st.write("")
    st.write("")
    
 #Grouping by year, month, season 
    mon_year_season = cb.groupby(['year', 'month', 'season'])['median_trip_duration'].median().reset_index()
    mon_year_season['month_year_season'] = mon_year_season['month'].astype(str) + ' ' + mon_year_season['year'].astype(str) + ' ' + mon_year_season['season']

    fig = px.line(mon_year_season, x = 'month_year_season', y = 'median_trip_duration', 
                  title = 'Number of Trips by Month, Year and Season',
                  labels = {'month_year_season': 'Month, Year and Season', 'median_trip_duration': 'Median Trip Duration'})

    fig.update_layout(width = 800, height = 600)
    fig.update_traces(mode = 'lines+markers')

    # Displaying 
    st.plotly_chart(fig)


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 

# Tab 3: Weather
with tab3:
    st.title('Weather')
    st.markdown("""
    - **The weather can significantly impact the number of bike trips and the length of the trip.**
    """)

    column_name = {
    'Precipitation': 'prcp',
    'Snow': 'snow',
    'Average Wind Speed': 'awnd',
    'Average Relative Humidity': 'rhav',
    'Minimum Relative Humidity': 'rhmn',
    'Maximum Relative Humidity': 'rhmx',
    'Maximum Temperature': 'tmax',
    'Minimum Temperature': 'tmin',
    'Average Temperature': 'tavg'
    }
    #Select a season
    season = st.selectbox(
    "Select a season",
    cb['season'].unique(),  
    placeholder = "Select season...",
)
    
    # Selecting a feature
    option = st.selectbox(
    "Select a feature",
    list(column_name.keys())
    )
    
    #getting data from the season that was selected.
    season_data = cb[cb['season'] == season]

    # Create a histogram the selected season data.
    fig = px.histogram(season_data, x = column_name[option], nbins = 20, 
                   title = f'Distribution of {option}',
                   labels = {column_name[option]: f'{option}', 'count': 'Frequency'}
                    )

# Showing plot
    st.plotly_chart(fig)


















































