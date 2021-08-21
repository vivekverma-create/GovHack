#app.py

# import app2_test
# import sp500_app
# import ComingSoon
# import DataChecker
import trafficVolume
import parking
import streamlit as st

st.sidebar.title('Navigation')
PAGES = {
    # "NBA": app2_test,
    # "SP500": sp500_app,
    # "Covid-19": ComingSoon,
    "Traffic Volume":trafficVolume,
    "Parking":parking
    # "Data Analysis":DataChecker
}
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()