import streamlit as st
import pandas as pd
import numpy as np

## Title
st.title("Simple Data Analysis App - Streamlit")

## Display a simple text
st.write("This app allows you to upload a CSV file and perform basic data analysis.")

## Create a dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## Display the dataframe
st.write("Here is a simple dataframe:")
st.dataframe(df)

## Line chart
st.write("Here is a line chart of the dataframe:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)