import streamlit as st

# Define a function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / ((height/100) ** 2)
    return bmi

# Define Streamlit app layout
st.title("BMI Calculator")

# Add input controls for name, gender, age, address, hobbies, weight, and height
name = st.text_input("Name")
gender = st.radio("Gender", ("Male", "Female", "Other"))
age = st.number_input("Age", min_value=0, max_value=120, step=1)
address = st.text_area("Address")
hobbies = st.multiselect("Hobbies", ("Reading", "Gaming", "Cooking", "Traveling", "Exercising"))
weight = st.number_input("Weight in kg", min_value=0.0, max_value=500.0, step=0.1)
height = st.number_input("Height in cm", min_value=0, max_value=300, step=1)

# Add a button to calculate BMI
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write(f"**BMI:** {bmi:.2f}")

