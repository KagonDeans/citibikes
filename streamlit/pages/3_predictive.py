import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm
import statsmodels.formula.api as smf
import shap
import xgboost


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer



st.title("Lets Make Predictions")

cb = pd.read_csv("../data/citibike_vis.csv")
x_test = pd.read_csv("../data/X_test.csv")

# Creating tabs
tab1, tab2 = st.tabs(["Predict The Number of Trips", "Predict The Median Trip Duration"])

# Tab 1: Trips
with tab1:
    st.markdown(""" I have developed a predictive model using the Scikit-learn linear regression algorithm. This model is designed to forecast the daily number of trips using the following set of features:
    
    - Maxium daily temperture
    - Average daily temperture
    - If it snowed 
    - If it rained 
    - Day of week 
    - If it was a holiday 
    - Season 
    - Month 
    - Average wind speed 
    - Average relative humidity  
    - Minimum Relative Humidity
    - Maximum Relative Humidity
    - Whether an event occured 
    """)
    
    st.markdown(""" 
After splitting my dataset into training and testing sets, I performed standardization and applied iterative imputation to handle missing data. I then fitted and predicted using a model with XGBoost. The results are as follows:

- R-squared (R^2) score: 0.688
- Mean Absolute Error (MAE): 12097
- Mean Squared Error (MSE): 240954429.49
- Standard Deviation (std): 27875.38
""")
    
    st.image(('../photos/shap.png'), caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image(('../photos/shap_bar.png'), caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    
    
with tab2:
    
    st.markdown(""" Using the same Scikit-learn linear regression algorithm, This model is designed to forecast the median trip duration using the following set of features:
    
    - Maxium daily temperture
    - Average daily temperture
    - If it snowed 
    - If it rained 
    - Day of week 
    - If it was a holiday 
    - Season 
    - Month 
    - Average wind speed 
    - Average relative humidity  
    - Minimum Relative Humidity
    - Maximum Relative Humidity
    - Whether an event occured 
    """)
    
    st.markdown(""" 
After splitting my dataset into training and testing sets, I performed standardization and applied iterative imputation to handle missing data. I then fitted and predicted using a model with XGBoost. The results are as follows:

- R-squared (R^2) score: 0.406
- Mean Absolute Error (MAE): 84.099
- Mean Squared Error (MSE): 12613.317
- Standard Deviation (std): 146.063
""")
    
    st.image(('../photos/shap_waterfall_med.png'), caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image(('../photos/shap_bar_med.png'), caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    
    
    
    
    
    
    
    
    
    
    
    
#     predictors = ['tmax', 'is_snow', 'did_rain', 'day_of_week', 'holiday', 'season', 'month', 'awnd', 'rhav', 'rhmn', 'rhmx', 'tavg', 'event_happened']
#     cat_predictors = ['is_snow', 'did_rain', 'day_of_week', 'holiday', 'season', 'month', 'event_happened']
#     num_predictors = ['tmax', 'rhav', 'rhmn', 'rhmx', 'tavg', 'awnd']

#     X = cb[predictors]
#     X = pd.get_dummies(X, columns = cat_predictors)
#     y = cb['num_of_trips']

#     # Splitting the X and y variables for training and testing
#     X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=117)

#     # Creating the scaler and imputer
#     scaler = StandardScaler()
#     iterative_imputer = IterativeImputer()

#     # Fit the scaler and imputer on the training set
#     X_train_num = scaler.fit_transform(X_train[num_predictors])
#     X_train_num = iterative_imputer.fit_transform(X_train_num)

#     # the same transformations to the test set
#     X_test_num = scaler.transform(X_test[num_predictors])
#     X_test_num = iterative_imputer.transform(X_test_num)

#     X_train.loc[:, num_predictors] = X_train_num
#     X_test.loc[:, num_predictors] = X_test_num

#     #linear regression model
#     linreg = LinearRegression()
#     linreg.fit(X_train, y_train)

#     # Predict on the test set
#     y_pred_all = linreg.predict(X_test)
#     xgb = xgboost.XGBRegressor(tree_method="hist", enable_categorical=True).fit(X_train, y_train)

    
#     explainer = shap.TreeExplainer(xgb)
#     explanation = explainer(X_test)

#     shap.summary_plot(explanation, X_test, plot_type = "bar")
#     st.pyplot()
   
    
    
    
    
    
    
    
    
    
#     lm = smf.ols('num_of_trips ~  tmax + tavg + rhav + prcp + season + holiday + did_rain + C(year) + C(day_of_week) + C(month)', data = cb).fit()
    
#     feature_name = {
#     'Week Days': [
#         ['C(day_of_week)[T.1]', 'C(day_of_week)[T.2]', 'C(day_of_week)[T.3]', 'C(day_of_week)[T.4]', 'C(day_of_week)[T.5]', 'C(day_of_week)[T.6]'],
#         ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     ],
#     'Season': [
#         ['season[T.Spring]', 'season[T.Summer]', 'season[T.Winter]'],
#         ['Spring', 'Summer', 'Winter']
#     ],
#     'Month': [
#         ['C(month)[T.2]', 'C(month)[T.3]', 'C(month)[T.4]', 'C(month)[T.5]', 'C(month)[T.6]', 'C(month)[T.7]', 'C(month)[T.8]', 'C(month)[T.9]', 'C(month)[T.10]', 'C(month)[T.11]', 'C(month)[T.12]'],
#         ['Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
#     ],
#     'Year' : [
#         ['C(year)[T.2020]', 'C(year)[T.2021]'],
#         ['2020Y', '2021Y']
#     ],
#     'Did Rain': [
#         ['did_rain[T.True]'],
#         ['Did Rain']
#     ],
#     'Holiday': [
#         ['holiday[T.True]'],
#         ['Holiday']
#     ]
    
# }
    
    
    
#     select_season = st.selectbox(
#     "Select a Season",
#     feature_name['Season'][1]
# )
#     select_day = st.selectbox(
#     "Select a Day",
#     feature_name['Week Days'][1]
# )
#     select_month = st.selectbox(
#     "Select a Month",
#     feature_name['Month'][1]
# )
#     select_year = st.selectbox(
#     "Select a Year",
#     feature_name['Year'][1]
# )

#     selected_season = select_season
#     selected_day = select_day
#     selected_month = select_month
#     selected_year = select_year 
    
    













# st.write("### Input Data")
# col1, col2 = st.columns(2)
# day_of_week = col1.text_input("Day of the Week")
# season = col1.text_input("Season")
# maxium_temp = col1.number_input("Max Temp (in F°)", min_value = 15, value = 98)

# st.write("### Num of Trips")
# col1 = st.columns(1)
# col1.metric(label = "Number of predicted trips")
