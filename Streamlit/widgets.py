## Wdiget means we'll try to make interactive applications

import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello, {name}")

##Age slider

age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is {age}")

## add options box
language = st.selectbox("Choose your favorite langugae: ", ["Python", "Java", "C++", "C-language", "Javascript"])
st.write(f"Your selceted language is: {language}")

## Display Dataframe
data = {'Name': ["Nairobi", "Mania", "Gandia", "Raquel", "Sergio"], 
        'Age': [36, 35, 42, 47, 50],
         "City": ["New_YORK", "Paris", "Los Angles", "Chicago", "Houston"]}


df = pd.DataFrame(data)
df.to_csv("Sample Data.csv")
st.write(df)

##Upload Csv file and convert it into dataframe
file = st.file_uploader("Choose a CSV file", type = "csv")

if file is not None:
    df_file = pd.read_csv(file)
    st.write(df_file)

