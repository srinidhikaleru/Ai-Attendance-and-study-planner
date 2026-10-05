import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# Student information
attendance = 62
study_hours = 3
marks = 52
days_to_exam = 20


# Give the information to the AI
prediction = model.predict([
    [
        attendance,
        study_hours,
        marks,
        days_to_exam
    ]
])


# Display prediction
print("Predicted Risk:", prediction[0])