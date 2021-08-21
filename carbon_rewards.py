import pandas as pd
import streamlit as st
import base64


def app():   
    st.title("Green Rewards!")  # add a title
    st.markdown("""
    This page shows simple visualisation of reduced carbon in Melbourne Region!
    """)

    image=("./carbon_emission_vehicle.JPG")
    st.image(image, caption='Carbon emission footprint', use_column_width=True)
    image1=("./passenger_kilometer.JPG")
    st.image(image1, caption='Billion passenger kilometer travelled', use_column_width=True)


