import pandas as pd
import streamlit as st
import base64

df = pd.read_csv("./pedestrian_density.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
# df = pd.read_excel(...)  # will work for Excel files
def app():   
    st.title("Melbourne Pedestrian Traffic Data!")  # add a title
    st.markdown("""
    This app visualise pedestrian density across Melbourne city using [open data](https://data.melbourne.vic.gov.au/widgets/b2ak-trbp)!
    """)
    st.markdown("""
    daily pedestrian density can be visualised [here](http://www.pedestrian.melbourne.vic.gov.au/#date=06-08-2021&time=22).
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
    image=("./pedestrian_data.JPG")
    st.image(image, caption='Inner Melbourne pedestrian density', use_column_width=True)
    image1=("./pedestrian.JPG")
    st.image(image1, caption='Comparison of passenger volumes for train, for AM peak - Train patronage decreases across all lines', use_column_width=True)


