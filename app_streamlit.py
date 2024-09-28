# demo to create an application in which the user can give two inputs and output is --> +, -, /, *

# application file --> app.py 

import streamlit as st

st.write("# Streamlit Basic Calculator")

# input two numbers 
number1 = st.number_input("Enter the first number", value=0.0)
number2 = st.number_input("Enter the second number", value=0.0)

# Initialize results
addition = None
subtraction = None
multiplication = None
division = None

# Perform the calculations 
if number1 is not None and number2 is not None:
    addition = number1 + number2
    subtraction = number1 - number2
    multiplication = number1 * number2
    
    # Handle division by zero
    if number2 != 0:
        division = number1 / number2
    else:
        division = "Undefined (cannot divide by zero)"

# Display results 
if addition is not None:
    st.write(f"The addition of {number1} and {number2} is {addition}")
    st.write(f"The subtraction of {number1} and {number2} is {subtraction}")
    st.write(f"The multiplication of {number1} and {number2} is {multiplication}")
    st.write(f"The division of {number1} and {number2} is {division}")
