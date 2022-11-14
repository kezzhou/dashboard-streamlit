#### Imports ####

import pandas as pd
import streamlit as st

#### First Dataframe - Head 100 ####

df = pd.read_csv('data_sparcs.csv')

df = df.head(100)

df

#### Header ####

if st.checkbox('Show first 100 records of SPARCS 2016'):
    st.header('Hospital Inpatient Discharges (SPARCS De-Identified): 2016')
    st.dataframe(df)


#### Caption ####

st.caption('The Statewide Planning and Research Cooperative System (SPARCS) Inpatient De-identified File contains discharge level detail on patient characteristics, diagnoses, treatments, services, and charges. This data file contains basic record level detail for the discharge. The de-identified data file does not contain data that is protected health information (PHI) under HIPAA. The health information is not individually identifiable; all data elements considered identifiable have been redacted. For example, the direct identifiers regarding a date have the day and month portion of the date removed.')

#### Code Block ####

code = '''## Wondering how we included the toggle feature?
if st.checkbox('Show first 100 records of SPARCS 2016'):
    st.header('Hospital Inpatient Discharges (SPARCS De-Identified): 2016')
    st.dataframe(df)'''
st.code(code, language='python')

#### Second Dataframe ####

df = pd.read_csv('data_sparcs.csv')

df2 = df[["Total Charges", "Total Costs"]]

df2

st.dataframe(df2)

#### Barchart - Race ####

df3 = df["Race"]

st.area_chart(df3)

#### Line Chart - Race and Total Costs ####

df4 = df[["Race", "Total Costs"]]

st.line_chart(df4)