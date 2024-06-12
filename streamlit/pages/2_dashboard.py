import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import statsmodels.formula.api as smf


cb = pd.read_csv("../data/citibike_vis.csv")

tab1, tab2 = st.tabs(["Number of Trips Linear Regression", "Median Trip Duration linear Regression"])
with tab1:
    st.markdown("""I completed a linear regression analysis using the OLS method from the statsmodels library. The initial model examined how various features influenced the number of trips taken per day. The features that were statistically significant included:

- The month
- Day of the week
- Season
- Year as catergories
- Maximum and average daily temperature
- Average Relative humidity
- Whether it rained and how much rain
- Whether it was a holiday 
""")

    st.write("")
    st.write("")
    st.write("")

    st.markdown("""Below the features you're able to select are categorical features that display the coefficients compared to the reference category which are:
- Days of the week: Monday
- Seasons: Fall
- Months: January
- Did it Rain: It did not rain
- Did it snow: It did not snow
- Is it a holiday: It is not a holiday
""")
    
    

#tavg + rhav + prcp + season + holiday + did_rain C(year) + C(day_of_week) + C(month)

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

    feature_trips = st.selectbox(
    "Select a Feature",
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
    reference_dict = {
    'Week Days': 'Monday',
    'Season': 'Fall',
    'Month': 'January',
    'Year': '2019',  
    'Did Rain': 'It did not rain',
    'Holiday': 'It is not a holiday'
}

    reference_variable = reference_dict.get(feature_trips)

    fig = px.bar(coeffs_df, x='Predictor', y='Coefficient', 
             title=f'Coefficients of {feature_trips} (Reference: {reference_variable})',
             labels={'Predictor': feature_trips, 'Coefficient': 'Coefficient of Trips per Day'})

    st.plotly_chart(fig)


    st.write("")
    st.write("")
    st.write("")

    new_feature_names = {
    'C(day_of_week)[T.1]': 'Tuesday',
    'C(day_of_week)[T.2]': 'Wednesday',
    'C(day_of_week)[T.3]': 'Thursday',
    'C(day_of_week)[T.4]': 'Friday',
    'C(day_of_week)[T.5]': 'Saturday',
    'C(day_of_week)[T.6]': 'Sunday',
    'season[T.Spring]': 'Spring',
    'season[T.Summer]': 'Summer',
    'season[T.Winter]': 'Winter',
    'C(month)[T.2]': 'Feb',
    'C(month)[T.3]': 'Mar',
    'C(month)[T.4]': 'Apr',
    'C(month)[T.5]': 'May',
    'C(month)[T.6]': 'June',
    'C(month)[T.7]': 'July',
    'C(month)[T.8]': 'Aug',
    'C(month)[T.9]': 'Sept',
    'C(month)[T.10]': 'Oct',
    'C(month)[T.11]': 'Nov',
    'C(month)[T.12]': 'Dec',
    'C(year)[T.2020]': '2020Y',
    'C(year)[T.2021]': '2021Y',
    'did_rain[T.True]': 'Did Rain',
    'holiday[T.True]': 'Holiday'
}

    st.markdown("""The table below displays all the features used with the target value, Number of trips & their coefficients:""")

    all_predictors = lm.params.index.drop('Intercept')  
    all_coefficients = lm.params.values[1:] 

    num_of_trips_coeff = pd.DataFrame({
    'Features': all_predictors,
    'Coefficients': all_coefficients
})

    num_of_trips_coeff['Features'] = num_of_trips_coeff['Features'].replace(new_feature_names)

    st.dataframe(num_of_trips_coeff, height=500, width=400)



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
st.write("")
st.write("")
st.write("")

with tab2:

    st.markdown("""For the linear regression analysis examining how various features influenced the how long a trip lasted. The features that were statistically significant included:

- The month
- Day of the week
- Season
- Year as catergories
- Maximum daily temperature
- Whether it snowed
- Average wind speed
- Whether it rained and how much rain
- Whether it was a holiday 
""")

    lm_med_len = smf.ols('median_trip_duration ~ tmax + prcp + awnd + season + holiday + did_rain + is_snow + C(month) + C(day_of_week) + C(year)', data = cb).fit()


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
    ],
    'Did Snow': [
        ['is_snow[T.True]'],
        ['Did Snow']
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
    reference_dict_med = {
    'Week Days': 'Monday',
    'Season': 'Fall',
    'Month': 'January',
    'Year': '2019',  
    'Did Rain': 'It did ot rain',
    'Holiday': 'It is not a holiday',
    'Did Snow': 'It did not snow'
}

    reference_variable_med = reference_dict_med.get(feature)

    fig = px.bar(coeffs_df, x='Predictor', y='Coefficient', 
             title=f'Coefficients of {feature} (Reference: {reference_variable_med})',
             labels={'Predictor': feature, 'Coefficient': 'Coefficient of Median Trip Duration'})

    st.plotly_chart(fig)

#     fig = px.bar(coeffs_df, x = 'Predictor', y = 'Coefficient', 
#              title = f'Coefficients of {feature}',
#              labels = {'Predictor': feature, 'Coefficient': 'Coefficient of Median Trip Duration'})

#     st.plotly_chart(fig)

    st.write("")
    st.write("")
    st.write("")

    st.markdown("""The table below displays all the features used with the target value, Median Trip Duration & their coefficients:""")

    new_feature_names = {
    'C(day_of_week)[T.1]': 'Tuesday',
    'C(day_of_week)[T.2]': 'Wednesday',
    'C(day_of_week)[T.3]': 'Thursday',
    'C(day_of_week)[T.4]': 'Friday',
    'C(day_of_week)[T.5]': 'Saturday',
    'C(day_of_week)[T.6]': 'Sunday',
    'season[T.Spring]': 'Spring',
    'season[T.Summer]': 'Summer',
    'season[T.Winter]': 'Winter',
    'C(month)[T.2]': 'Feb',
    'C(month)[T.3]': 'Mar',
    'C(month)[T.4]': 'Apr',
    'C(month)[T.5]': 'May',
    'C(month)[T.6]': 'June',
    'C(month)[T.7]': 'July',
    'C(month)[T.8]': 'Aug',
    'C(month)[T.9]': 'Sept',
    'C(month)[T.10]': 'Oct',
    'C(month)[T.11]': 'Nov',
    'C(month)[T.12]': 'Dec',
    'C(year)[T.2020]': '2020Y',
    'C(year)[T.2021]': '2021Y',
    'did_rain[T.True]': 'Did Rain',
    'holiday[T.True]': 'Holiday',
    'is_snow[T.True]': 'Did snow'
}

    all_predictors = lm_med_len.params.index.drop('Intercept')  
    all_coefficients = lm_med_len.params.values[1:] 

    median_trip_len_coeff = pd.DataFrame({
    'Features': all_predictors,
    'Coefficients': all_coefficients
})

    median_trip_len_coeff['Features'] = median_trip_len_coeff['Features'].replace(new_feature_names)

    st.dataframe(median_trip_len_coeff, height=500, width=400)

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX































