#app.py

# import app2_test
# import sp500_app
# import ComingSoon
# import DataChecker
import trafficVolume
import parking
import carbon_rewards
import pedestrian
import streamlit as st

st.sidebar.title('Navigation')
PAGES = {
    "Traffic Volume":trafficVolume,
    "Parking":parking,
    "Pedestrian":pedestrian,
    "Green Rewards":carbon_rewards,


}
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()