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
    
    
    
    
    
    
    
    
    
    
    
    

