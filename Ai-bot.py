import streamlit as st
import math

st.title("MathBot - Smart Calculator 🤖")

operation = st.selectbox(
    "Choose an operation:",
    ["Addition", "Subtraction", "Multiplication", "Division", "Square", "Square Root", "Factorial"]
)

# Input logic: single number vs two numbers
if operation in ["Square", "Square Root", "Factorial"]:
    num1 = st.number_input("Enter a number:", value=0.0)
else:
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)

if st.button("Calculate"):
    try:
        if operation == "Addition":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtraction":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiplication":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Division":
            if num2 == 0:
                st.error("❌ Division by zero is not allowed!")
            else:
                st.success(f"Result: {num1 / num2}")
        elif operation == "Square":
            st.success(f"Result: {num1 ** 2}")
        elif operation == "Square Root":
            if num1 < 0:
                st.error("❌ Cannot calculate square root of a negative number!")
            else:
                st.success(f"Result: {math.sqrt(num1)}")
        elif operation == "Factorial":
            if num1 < 0 or not float(num1).is_integer():
                st.error("❌ Factorial only works with non-negative integers!")
            else:
                st.success(f"Result: {math.factorial(int(num1))}")
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
