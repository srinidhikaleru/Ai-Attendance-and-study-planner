# Import Streamlit
import streamlit as st

# Import pickle
import pickle


# Load the trained AI model
with open("model.pkl", "rb") as file:

    model = pickle.load(file)


# Page configuration
st.set_page_config(
    page_title="AI Attendance & Study Planner",
    page_icon="🎓"
)


# Main title
st.title("🎓 AI Attendance & Study Planner")


# Description
st.write(
    "Enter your academic details to predict your academic risk."
)


# Student name
name = st.text_input(
    "Enter your name"
)


# Attendance
attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=75.0
)


# Study hours
study_hours = st.number_input(
    "Study Hours Per Week",
    min_value=0.0,
    max_value=50.0,
    value=5.0
)


# Recent marks
marks = st.number_input(
    "Recent Marks (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)


# Days until exam
days_to_exam = st.number_input(
    "Days Until Exam",
    min_value=1,
    max_value=365,
    value=30
)


# Prediction button
if st.button("🤖 Predict Risk"):

    # Send student information to the model
    prediction = model.predict([
        [
            attendance,
            study_hours,
            marks,
            days_to_exam
        ]
    ])


    # Get prediction result
    risk = prediction[0]


    # Display result
    st.subheader("AI Prediction")


    if risk == "High":

        st.error("🔴 High Academic Risk")

    elif risk == "Medium":

        st.warning("🟡 Medium Academic Risk")

    else:

        st.success("🟢 Low Academic Risk")