import streamlit as st
import pandas as pd


st.title("Pedal Forward: Analyzing and Predicting Citibike Usage in NYC")



st.image(('../photos/p-1-lyft-puts-the-brakes-on-some-of-its-citi-bikes-due-to-brake-issues.jpg'), caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.markdown(
    """
    <div style="text-align: center;">
        <h2>By Kagon Deans DS7</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# st.page_link(overview, label = 'overview', icon = None)


# st.link_button("🚲 Let's take a ride 🚲 ", url  = '/overview') 


# Define the target page function
def overview():
    st.write("Welcome to the overview page!")

# Set up session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'bike'

# Define navigation function
def navigate_to_overview():
    st.session_state.page = 'overview'

# Main app
if st.session_state.page == 'bike':
    if st.button("🚲 Let's take a ride 🚲"):
        navigate_to_overview()
    st.write("This is the bike page.")
elif st.session_state.page == 'overview':
    overview()
