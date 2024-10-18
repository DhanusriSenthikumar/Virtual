import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title("Simple Streamlit App")

# Sidebar for user input
st.sidebar.header("Input Parameters")

# Text input in the sidebar
user_name = st.sidebar.text_input("Enter your name", "John Doe")

# Slider input in the sidebar
age = st.sidebar.slider("Select your age", 0, 100, 25)

# Dropdown (select box) input
option = st.sidebar.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])

# Button to submit
if st.sidebar.button("Submit"):
    st.write(f"Hello, {user_name}! You selected {option} and are {age} years old.")

# Generating sample data
data = np.random.randn(50, 3)
df = pd.DataFrame(data, columns=["Column 1", "Column 2", "Column 3"])

# Displaying the DataFrame
st.subheader("Sample Data")
st.write(df)

# Plotting a simple chart
st.subheader("Data Visualization")
st.line_chart(df)

# Adding a simple Matplotlib plot
st.subheader("Matplotlib Chart")
fig, ax = plt.subplots()
ax.scatter(df["Column 1"], df["Column 2"], color='green')
ax.set_title("Scatter plot of Column 1 vs Column 2")
ax.set_xlabel("Column 1")
ax.set_ylabel("Column 2")
st.pyplot(fig)
