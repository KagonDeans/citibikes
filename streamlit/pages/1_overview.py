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

    st.markdown("""
Let's break down the citibike data:

- 2019: **20,551,697**
- 2020: **19,506,857**
- 2021: **27,661,451**

In total, there were **67,720,005** bike rides.
""")

    st.write("")
    
    #adding all years to years list
    year_options = ['All Years'] + cb['year'].unique().tolist()

    #Select a year
    select_year = st.selectbox(
    "Select a year",
    year_options
)

    #selected year will show data for that year
    if select_year == 'All Years':
        years = cb
    else:
        years = cb[cb['year'] == select_year]
    
    
    # Days of week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Grouping by day of the week and summing the number of trips.
    daily_trips = years.groupby('day_of_week')['num_of_trips'].sum().reset_index()

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
    seasonal_trips = years.groupby('season')['num_of_trips'].sum().reset_index()

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
    
    cb['median_trip_duration'] = cb['median_trip_duration'] / 60
    cb['mean_trip_duration'] = cb['mean_trip_duration'] / 60

    med_trip_dur = round(cb['median_trip_duration'].median())
    mean_trip_dur = round(cb['mean_trip_duration'].mean())
    yearly_med_trip_dur = cb.groupby('year')['median_trip_duration'].median().round()

    st.markdown(f"""
    - **The median trip duration is {med_trip_dur} minutes**
    - **Average trip duration: {mean_trip_dur} minutes**
    """)

    st.write(yearly_med_trip_dur)
    
    
    
    #adding all years to years list
    year_options = ['All Years'] + cb['year'].unique().tolist()

    #Select a year
    select_year_med = st.selectbox(
    "Select year",
    year_options
)

    #selected year will show data for that year
    if select_year_med == 'All Years':
        years = cb
    else:
        years = cb[cb['year'] == select_year_med]
    
    # days of week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # Grouping by day of the week and calculating the median trip duration
    med_trip_duration = years.groupby('day_of_week')['median_trip_duration'].median().reset_index()

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
    seasonal_trips = years.groupby('season')['median_trip_duration'].median().reset_index()

    # Plotting a box plot
    fig = px.box(years, x = 'season', y = 'median_trip_duration', title = 'Median Trip Durations by Season')
    fig.update_layout(width = 800, height = 600)

    # Showing the plot
    st.plotly_chart(fig)

    st.write("")
    st.write("")
    st.write("")
    
 #Grouping by year, month, season 

#     month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
#               7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    
#     cb['month'] = cb['month'].map(month_dict)

    
    mon_year_season = cb.groupby(['year', 'month', 'season'])['median_trip_duration'].median().reset_index()
    mon_year_season['month_year_season'] = mon_year_season['month'].astype(str) + ' ' + mon_year_season['year'].astype(str) + ' ' + mon_year_season['season']

    fig = px.line(mon_year_season, x = 'month_year_season', y = 'median_trip_duration', 
                  title = 'Median Trip Duration by Month, Year and Season',
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
    The weather data had over 50 columns filled with data, many of them were missing more than half their data. I decided using the following weather data:
    - Precipitation
    - Snow
    - Average Wind Speed
    - Average Relative Humidity
    - Minimum Relative Humidity
    - Maximum Relative Humidity
    - Maximum Temperature
    - Minimum Temperature
    - Average Temperature
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
    #adding all years to years list
    year_options = ['All Years'] + cb['year'].unique().tolist()

    #Select a year
    select_year_weather = st.selectbox(
    "Choose Year",
    year_options
)

    #selected year will show data for that year
    if select_year_weather == 'All Years':
        years = cb
    else:
        years = cb[cb['year'] == select_year_weather]
    
    # Selecting a feature
    option = st.selectbox(
    "Select a feature",
    list(column_name.keys())
    )

    # Create a histogram the selected season data.
    fig = px.histogram(years, x = column_name[option], nbins = 20, 
                   title = f'Distribution of {option}',
                   labels = {column_name[option]: f'{option}', 'count': 'Frequency'},
                    facet_col ='season'
                    )

# Showing plot
    st.plotly_chart(fig)


















































