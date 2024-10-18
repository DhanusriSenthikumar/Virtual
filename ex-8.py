import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title('Simple Streamlit App')

# Sidebar for user input
st.sidebar.header('User Input')

# Create a form for user input
name = st.sidebar.text_input('Your Name', '')
age = st.sidebar.slider('Your Age', 1, 100, 25)

# Submit button
if st.sidebar.button('Submit'):
    st.write(f'Hello, {name}! You are {age} years old.')

# Dataframe example
st.subheader('Sample Data')

# Create some sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 20, 15, 30]}

df = pd.DataFrame(data)
st.write(df)

# Plot the data
st.subheader('Bar Chart of Values')
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Values'])
st.pyplot(fig)
