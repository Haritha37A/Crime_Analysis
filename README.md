# Los Angeles Crime Data Dashboard (2020-2023)

This project is a data dashboard built with Streamlit to visualize crime data in Los Angeles from 2020 to 2023. The dashboard enables users to explore crime trends, distributions, and hotspots across the city, providing valuable insights through charts, maps, and data filtering options.

## Dataset
The dataset used is **"Crime_Data_from_2020_to_Present.csv"**. It includes information about:
- Dates of crime occurrence and reporting
- Area names and geographic coordinates
- Victim details (age, sex)
- Crime details (weapon type, crime frequency)

## Project Features
- **Data Preview**: View the initial dataset and missing value information.
- **Filters**: Select data by month, area, age group, and weapon type.
- **Charts**:
  - **Crime Trend Over Time**: Shows crime patterns over months and years.
  - **Crime Distribution by Area**: Displays the count of crimes per area.
  - **Age-Wise and Weapon-Wise Distributions**: Shows crimes by victim age group and weapon type.
  - **Correlation Matrix**: Displays relationships between numeric variables.
- **Maps**:
  - **Crime Hotspots**: Shows crime locations on a map.
  - **Crime Frequency Map**: Highlights areas with high, medium, or low crime frequency.

## How to Run the Project

1. **Install the Required Libraries**:
   - Make sure you have Python 3.12 installed.
   - Install dependencies with:
     ```bash
     pip install pandas streamlit matplotlib seaborn folium streamlit_folium
     ```

2. **Run the Streamlit App**:
   - Place the dataset file **"Crime_Data_from_2020_to_Present.csv"** in the project directory.
   - Run the app with:
     ```bash
     streamlit run app.py
     ```
     ## Deployed App

You can access the deployed Crime Analysis app here:

[Crime Analysis App](https://crimeanalysis-n5yuxqmsy7z7rb9vgzxken.streamlit.app/)

3. **Explore the Dashboard**:
   - Open the app in your browser (usually at [http://localhost:8511](http://localhost:8511)) and use the filters to explore the crime data.

## Acknowledgments
- **Data Source**: Kaggle - *Los Angeles Crime Data (2020-2023)*

