# citibikes

***Pedal Forward: Exploring Citibike Usage in NYC***

*Project Overview*

I developed an interactive streamlit application to explore the factors that influences bike usage in NYC using citibike.

*Motivation*

I chose this topic due to my interest in transportation and the unique nature of bike riding, which can be both a necessity and a leisure activity. I aimed to understand the conditions under which most bike rides occur.

*Challenges and Approach*

I worked with Citibike data spanning the years 2019, 2020, and 2021, totaling over 60 million records. Handling this large dataset was challenging due to computational constraints. To manage this, I processed each year's data separately and condensed it to daily records. Another challenge was balancing the need to explore interesting data while staying focused on the project's goals.
*Data Source and Tools*

Citibike data: [here](https://s3.amazonaws.com/tripdata/index.html) with a total of 67,706,806 records used throughout the project.

Weather data: [here](https://www.ncei.noaa.gov/access/search/data-search/daily-summaries?bbox=40.963,-74.257,40.463,-73.757&startDate=2019-01-01T00:00:00&endDate=2022-12-31T23:59:59), Collected from the NYC Central Park weather station. Originally containing 59 variables, I used 9 relevant variables after filtering out missing and irrelevant data. 

The tools used are:

• Python for data handling and analysis.
• Streamlit for building the interactive dashboard.

*Usage*

My dashboard consists of 3 pages, each offering unique functionalities:

The introductory page provides a comprehensive breakdown of the two datasets pivotal to my project: the Citibike data and the weather dataset. Here, you'll discover insightful details such as the annual trip count and how they break down by days of the week, months, and seasons. 

With a focus on the median trip duration, the second tab of the overview page offers a detailed analysis of this metric across year, day of the week, and season.

Transitioning to the third tab, attention shifts to the weather data. Within this section, you can explore the diverse weather variables analyzed during the project, alongside their distribution across different years and seasons.

On the second page, titled "The Linear Regression Page," I showcase the outcomes of my linear regression analyses using the OLS method from the statsmodels library. I've created two models: one to analyze the daily count of trips and another to examine the median trip duration. In each model, I present the coefficients of the selected variables, providing insights into their relationships.

On the third tab, labeled "Predictive" I showcasel the outcomes of a predictive model employing the same dependent variables explored on the second page. For this analysis, I opted for Scikit-learn's linear regression algorithm.

In this predictive model, I demonstrate how the selected independent variables contribute to forecasting the daily count of trips and the median trip duration.

*Future Goals*
TBA
