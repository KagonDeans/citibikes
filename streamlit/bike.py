import streamlit as st
import pandas as pd


st.title("Pedal Forward: Analyzing and Predicting Citibike Usage in NYC")



st.image(('../photos/p-1-lyft-puts-the-brakes-on-some-of-its-citi-bikes-due-to-brake-issues.jpg'), caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.markdown(
    """
    <div style="text-align: center;">
        <h2>Kagon Deans DS7</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.page_link(page  = 'pages/1_overview.py',  label  = "🚲 Let's take a ride 🚲 ")
