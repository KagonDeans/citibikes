import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import statsmodels.formula.api as smf


st.title("Lets Make Predictions")

cb = pd.read_csv("../data/citibike_vis.csv")

# Creating tabs
tab1, tab2 = st.tabs(["Predict The Number of Trips", "Predict The Median Trip Duration"])

# Tab 1: Trips
with tab1:
    lm = smf.ols('num_of_trips ~  tmax + tavg + rhav + prcp + season + holiday + did_rain + C(year) + C(day_of_week) + C(month)', data = cb).fit()
    
    feature_name = {
    'Week Days': [
        ['C(day_of_week)[T.1]', 'C(day_of_week)[T.2]', 'C(day_of_week)[T.3]', 'C(day_of_week)[T.4]', 'C(day_of_week)[T.5]', 'C(day_of_week)[T.6]'],
        ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ],
    'Season': [
        ['season[T.Spring]', 'season[T.Summer]', 'season[T.Winter]'],
        ['Spring', 'Summer', 'Winter']
    ],
    'Month': [
        ['C(month)[T.2]', 'C(month)[T.3]', 'C(month)[T.4]', 'C(month)[T.5]', 'C(month)[T.6]', 'C(month)[T.7]', 'C(month)[T.8]', 'C(month)[T.9]', 'C(month)[T.10]', 'C(month)[T.11]', 'C(month)[T.12]'],
        ['Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
    ],
    'Year' : [
        ['C(year)[T.2020]', 'C(year)[T.2021]'],
        ['2020Y', '2021Y']
    ],
    'Did Rain': [
        ['did_rain[T.True]'],
        ['Did Rain']
    ],
    'Holiday': [
        ['holiday[T.True]'],
        ['Holiday']
    ]
    
}
    
    
    
    
    
    select_season = st.selectbox(
    "Select a Season",
    feature_name['Season'][1]
)
    select_day = st.selectbox(
    "Select a Day",
    feature_name['Week Days'][1]
)
    select_month = st.selectbox(
    "Select a Month",
    feature_name['Month'][1]
)
    select_year = st.selectbox(
    "Select a Year",
    feature_name['Year'][1]
)
    select_rain = st.selectbox(
    "Select if it Rained",
    feature_name['Did Rain'][1]
)
    select_Holiday = st.selectbox(
    "Select If it's a Holiday",
    feature_name['Holiday'][1]
)















# st.write("### Input Data")
# col1, col2 = st.columns(2)
# day_of_week = col1.text_input("Day of the Week")
# season = col1.text_input("Season")
# maxium_temp = col1.number_input("Max Temp (in F°)", min_value = 15, value = 98)

# st.write("### Num of Trips")
# col1 = st.columns(1)
# col1.metric(label = "Number of predicted trips")
