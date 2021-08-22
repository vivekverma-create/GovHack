import pandas as pd
import streamlit as st
import base64

df = pd.read_csv("./On-street_Parking_Bay_Sensors.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files
def app():   
    st.title("On-Street parking Data!")  # add a title
    st.markdown("""
    This app shows simple visualisation of avaliable parking in Inner Melbourne using city of Melbourne [open data](https://data.melbourne.vic.gov.au/Transport/On-street-Parking-Bay-Sensors/vh2v-4nfs)!
    """)
    st.write('Data Dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns.')
#     st.write(df)

    def filedownload(df):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
            href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
            return href

    
    filtered = st.sidebar.multiselect("Filter columns", options=list(df.columns), default=list(df.columns))
    st.markdown(filedownload(df), unsafe_allow_html=True)
    st.dataframe(df[filtered])
    image=("./parking.png")
    st.image(image, caption='Parking occupancy Inner Melbourne', use_column_width=True)
    image1=("./without_parkapp.JPG")
    st.image(image1, caption='Finding parking in normal scenario', use_column_width=True)
    image2=("./with_parkapp.JPG")
    st.image(image2, caption='Travelling to destination by knowing parking location and avaliability', use_column_width=True)
    image3=("./Destination1.PNG")
    st.image(image3, caption='Start to destination', use_column_width=True)
    image4=("./Destination.PNG")
    st.image(image4, caption='Start to destination with parking', use_column_width=True)
    st.markdown("""
    This can be integrated with Park and ride
    """)


