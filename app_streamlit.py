# demo to create a application in which the user can give two inputs and output is --> +,-,/, * 

# application file --> app.py 

import streamlit as st

st.write("# Streamlit Basic Calculator")

# input two numbers 

number1 = st.number_input("Enter the first number")
number2 = st.number_input("Enter the second number")

# perform the calculations 

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2


# Display my results 

st.write(f"The addition of {number1} and {number2} is {addition}")
st.write(f"The subtraction of {number1} and {number2} is {subtraction}")
st.write(f"The multiplication of {number1} and {number2} is {multiplication}")
st.write(f"The division of {number1} and {number2} is {division}")

