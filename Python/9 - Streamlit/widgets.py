import streamlit as st
import pandas as pd
import numpy as np

options = ['Python', 'Java', 'C++', 'JavaScript ']

st.title("Simple widgets app - Streamlit")

name=st.text_input("Enter your name:")
age=st.slider("Select your age:",0,100,25)
choice=st.selectbox("Select your favorite programming language:",options)

if name and age and choice:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old.")
    st.write(f"Your favorite programming language is {choice}.")


data = {
    "name": ['Lucas', 'Emma', 'Noah', 'Olivia'],
    "age": [23, 30, 22, 25],
    "favorite_language": ['Python', 'Java', 'C++', 'JavaScript ']
}

df = pd.DataFrame(data)
st.write("Here is the users favorite langue and them age:")
st.dataframe(df)

st.write('Upload a CSV file for analysis:')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("Here is the uploaded CSV file:")
    st.dataframe(uploaded_df)