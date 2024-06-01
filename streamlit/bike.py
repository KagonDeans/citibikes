import streamlit as st
import pandas as pd

st.title('Finally')
st.write('it works')

x = st.text_input("Favorite Movie")
st.write(f"Your favorite movie is: {x}")

is_clicked = st.button("Click Me")

st.write("## This is a H2 Title!")

citibikes = pd.read_csv("../data/citibike_vis.csv")
st.write(citibikes)


st.link_button("Profile", url = "/profile")








