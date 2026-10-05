# Import pandas to read the dataset
import pandas as pd

# Import Random Forest classifier
from sklearn.ensemble import RandomForestClassifier

# Import train_test_split
from sklearn.model_selection import train_test_split

# Import accuracy_score
from sklearn.metrics import accuracy_score

# Import pickle to save the trained model
import pickle


# Read the dataset
data = pd.read_csv("dataset.csv")


# Select input features
X = data[
    [
        "attendance",
        "study_hours",
        "marks",
        "days_to_exam"
    ]
]


# Select the target/output
y = data["risk"]


# Divide data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, y_train)


# Make predictions
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(
    y_test,
    y_pred
)


# Display accuracy
print("Model Accuracy:", accuracy)


# Save the trained model
with open("model.pkl", "wb") as file:

    pickle.dump(model, file)


# Display success message
print("Model saved successfully!")