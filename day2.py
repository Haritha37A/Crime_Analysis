import pandas as pd
import streamlit as st
df= pd.read_csv("Crime_Data_from_2020_to_Present.csv")
st.dataframe(df.head(10))

