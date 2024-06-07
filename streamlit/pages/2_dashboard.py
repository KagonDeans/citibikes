import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import statsmodels.formula.api as smf


cb = pd.read_csv("../data/citibike_vis.csv")

lm_med_len = smf.ols('median_trip_duration ~ tmax + season + C(year) + C(month) + holiday + did_rain + is_snow + C(day_of_week) ', data = cb).fit()

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
    ]
}

feature = st.selectbox(
    "Select a Predictor",
    feature_name.keys()
)

predictors = feature_name[feature][0]
labels = feature_name[feature][1]

coef = lm_med_len.params
coeffs = coef[predictors]
coeffs_df = pd.DataFrame({
    'Predictor': labels,
    'Coefficient': coeffs.values
})

fig = px.bar(coeffs_df, x='Predictor', y='Coefficient', 
             title = 'Coefficients of Predictors',
             labels = {'Predictor': 'Predictor', 'Coefficient': 'Coefficient in Seconds'})

st.plotly_chart(fig)


#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


lm = smf.ols('num_of_trips ~ + season + C(day_of_week) + tmax  + holiday + did_rain + awnd + rhav + rhmx + rhmn + tavg + event_happened + C(month)', data = cb).fit()

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
    ]
}

feature_trips = st.selectbox(
    "Select a Predictor_2",
    feature_name.keys()
)

predictors = feature_name[feature_trips][0]
labels = feature_name[feature_trips][1]

coef = lm.params
coeffs = coef[predictors]
coeffs_df = pd.DataFrame({
    'Predictor': labels,
    'Coefficient': coeffs.values
})

fig = px.bar(coeffs_df, x='Predictor', y='Coefficient', 
             title = 'Coefficients of Predictors',
             labels = {'Predictor': 'Predictor', 'Coefficient': 'Coefficient of trips per by'})

st.plotly_chart(fig)





























