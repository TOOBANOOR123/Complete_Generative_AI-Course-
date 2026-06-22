import streamlit as st
import pandas as pd
import numpy as np

st.title("My Streamlit App")
#Display some text 
st.write("Hello, The learning is fun")

##diplay a dataframe 
st.write("Here is the Datframe:")
df = pd.DataFrame({"Name": ["Aly", "Tokyo", "Denver", "Lisbon"],
                   "Age": [24, 38, 27, 45]})
st.write(df)
                
## Display a Line Chart 
st.write("Here is the Line Chart:")
line_chart = pd.DataFrame(np.random.rand(20, 3), columns = ['a', 'b', 'c'])
st.line_chart(line_chart)

