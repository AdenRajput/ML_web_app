"""
## App: Automobile EDA App
Author: [Aden Rajput](https://github.com/AdenRajput))\n

Description
This is a simple Exploratory Data Analysis of the Automobile Dataset depicting the various
car types and brands built with Streamlit.
We can preview the dataset,column names as well as show some basic plot with matplotlib and
seaborn.
Purpose
To show a simple EDA of Automobile data using Streamlit framework.

"""
# Import lib
import matplotlib
from distutils.command.upload import upload
import pandas as pd
import numpy as np
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
import plotly.express as px

# Some text
st.title("Automobile EDA App")
st.subheader("EDA Web App with Streamlit by Aden Rajput. ")
st.markdown(
        """
		#### Description
		+ This is an Exploratory Data Analysis  of the Automobile Dataset depicting the various makes and models built with Streamlit.

		#### Purpose
		+ To show a simple EDA of Automobile using Streamlit framework.
		""")

#dataset
matplotlib.use("Agg")  # Prevent runtime error due to tk
df = pd.read_csv("https://raw.githubusercontent.com/AdenRajput/ML_web_app/main/automobile_data.csv")

#EDA -- pandas profiling
pr = ProfileReport(df,explorative=True)
st.header('**Input DF**')
st.write(df)
st.write('---')
st.header('**Profiling report with pandas**')
st_profile_report(pr)

#data managemnt
make_option = df['make'].unique().tolist()
make = st.selectbox("Which Brand should we plot?",make_option,0)
df = df[df['make']==make]


# plotting
st.header('**Plotting Automobile data with Plotly **')
st.text("This graph compares the car mileages within city VS on highway along the price with respect to the body type.")
fig = px.scatter(df, x='city_mpg',y='highway_mpg',size='engine_size',color='price',hover_name='body_style',
                 log_x=True,size_max=55,range_x=[10,60],range_y=[10,60])

st.write(fig)