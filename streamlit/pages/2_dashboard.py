import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import statsmodels.formula.api as smf


cb = pd.read_csv("../data/citibike_vis.csv")

st.write("# Coef")

# # Days of week
#     days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
#     # Grouping by day of the week and summing the number of trips.
#     daily_trips = cb.groupby('day_of_week')['num_of_trips'].sum().reset_index()

#     # Plotting 
#     fig = px.bar(daily_trips, x = 'day_of_week', y = 'num_of_trips', 
#                     title = 'Total Number of Trips per Day of the Week', 
#                     labels = {'day_of_week': 'Day of the Week', 'num_of_trips': 'Total Number of Trips'},
#                     category_orders = {'day_of_week': days})

#     # Update tick labels
#     fig.update_layout(xaxis = {'tickvals':  daily_trips['day_of_week'], 'ticktext': days})
    
#     # Showing
#     st.plotly_chart(fig)


lm = smf.ols('num_of_trips ~ + season + day_of_week + tmax  + holiday + did_rain + awnd + rhav + rhmx + rhmn + tavg + event_happened', data = cb).fit()

#Graphing day of the week coefficients when controling for season, max temp, a holiday, & rain
predictors = ['day_of_week[T.1]', 'day_of_week[T.2]', 'day_of_week[T.3]', 'day_of_week[T.4]', 'day_of_week[T.5]', 'day_of_week[T.6]']

coef = lm.params
coeffs = coef[predictors]
coeffs_df = pd.DataFrame({
    'Predictor': ['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Coefficient': coeffs.values
})


fig = px.bar(coeffs_df, x='Predictor', y='Coefficient', 
             title='Coefficients of Predictors',
             labels={'Predictor': 'Day of the Week', 'Coefficient': 'Coefficient'})





















