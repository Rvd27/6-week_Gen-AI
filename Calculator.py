import streamlit as st

# Title
st.title("Simple Calculator App")

# User inputs
num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

# Operation selection
operation = st.selectbox(
    "Choose Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Button
if st.button("Calculate"):

    # Addition
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {result}")

    # Subtraction
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {result}")

    # Multiplication
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {result}")

    # Division
    elif operation == "Division":

        # Avoid divide by zero
        if num2 != 0:
            result = num1 / num2
            st.success(f"Result: {result}")
        else:
            st.error("Cannot divide by zero")