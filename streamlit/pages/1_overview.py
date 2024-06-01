import streamlit as st
import pandas as pd
import numpy as np
st.write("#overview")

cb = pd.read_csv("../data/cb_stream.csv")
#st.write(cb)

st.image("../photos/Total_trips.png")
st.write("In total there were 67,720,005 bikes rides")

st.bar_chart(data=cb, x='year', y='num_of_trips', color=None, width=None, height=None, use_container_width=True)

