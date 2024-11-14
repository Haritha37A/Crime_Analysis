import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

# Load the data
df = pd.read_csv("Crime_Data_from_2020_to_Present.csv")

st.dataframe(df.head(5))