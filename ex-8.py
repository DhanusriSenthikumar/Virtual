import streamlit as st

# Title of the app
st.title('Sample Survey')

# Header
st.header('Explore Different Features')

# Text input with a placeholder
name = st.text_input('What’s your name?', placeholder='Type your name here')

# Display greeting based on input
if name:
    st.success(f'Nice to meet you, {name}!')

# Radio buttons to choose a favorite color
color = st.radio("What's your favorite color?", ('Red', 'Green', 'Blue'))

# Display color selection
st.write(f'You chose: {color}')

# Number input instead of a slider
age = st.number_input('Enter your age', min_value=0, max_value=120, value=18)

# Display the age entered
st.info(f'You are {age} years old.')

# Toggle switch
like_coding = st.checkbox('Do you like coding?')

if like_coding:
    st.balloons()  # Fun element
    st.write("That's awesome! Keep coding!")

# Button with action
if st.button('Submit'):
    st.write('Thank you for your input!')

# Sidebar with a selectbox
st.sidebar.title('Additional Options')
option = st.sidebar.selectbox('Select your mood:', ['Happy', 'Neutral', 'Sad'])

st.sidebar.write(f'You are feeling: {option}')
