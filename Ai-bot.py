import re
import math
import streamlit as st

st.title("MathBot-AI powered Calculator")

operation=st.selectbox("Operation",["Add","subtract","Multiply","Divide","square","Root","Power","Factorial",])

num1=st.number_input("First Number")
num2=st.number_input("Second Number")

if st.button("Calculate"):
    result=None

    if operation=="Add":
        result = num1 + num2

    elif operation=="subtract":
        result = num1 - num2

    elif operation=="Multiply":
        result = num1 * num2

    elif operation=="Divide":
        if num2 !=0:
            result = num1 / num2
        else:
            result="Error: Cannot divide by zero"

    elif operation=="Square Root":
        result = math.sqrt(num1)

    elif operation=="power":
        result = math.pow(num1,num2)

    elif operation=="Factorial":
        result = math.factorial(int(num2))

    st.success(f"Result: {result}")