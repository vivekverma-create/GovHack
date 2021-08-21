import pandas as pd
import streamlit as st
import base64

df = pd.read_csv("./Traffic_Volume.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files
def app():   
    st.title("Victoria Traffic Data!")  # add a title
    st.markdown("""
    This app visualise transportation usage across Melbourne using city of Melbourne [open data](https://vicroadsopendata-vicroadsmaps.opendata.arcgis.com/datasets/vicroadsmaps::traffic-volume/about)!
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
    image=("./car_volume_increases.JPG")
    st.image(image, caption='Inner Melbourne car volume increases', use_column_width=True)
    image1=("./train_am_peak.JPG")
    st.image(image1, caption='Comparison of passenger volumes for train, for AM peak - Train patronage decreases across all lines', use_column_width=True)
    image2=("./tram_am_peak.JPG")
    st.image(image2, caption='Comparison of passenger volumes for tram, for AM peak - Tram patronage decreases across all lines', use_column_width=True)
    image3=("./bus_am_peak.JPG")
    st.image(image3, caption='Comparison of passenger volumes for Bus, for AM peak - Bus patronage decreases across all lines', use_column_width=True)
