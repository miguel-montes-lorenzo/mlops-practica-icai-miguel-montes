import os

import joblib
import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# ---------------------------
# MLFLOW CONFIGURATION
# ---------------------------

# Get the MLflow tracking server URI from an environment variable
# (in this case, it will point to the remote Dagshub server)
# remember to register / export the environment variable beforehand
tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")

# Configure MLflow to log experiments, metrics, and models to that URI
mlflow.set_tracking_uri(tracking_uri)

# ---------------------------
# DATA LOADING
# ---------------------------

# (p2.1)
# iris = datasets.load_iris()  (p2.1)
# X = iris.data
# y = iris.target

# (p3.2) substitute by this in p3.2
try:
    iris = pd.read_csv("data/iris_dataset.csv")
except FileNotFoundError:
    print("Error: The file 'data/iris_dataset.csv' was not found.")
    raise

X = iris.drop("target", axis=1)
y = iris["target"]

# ---------------------------
# MLFLOW EXPERIMENT
# ---------------------------

# Start a new MLflow run.
# Everything logged inside this block will be associated with this experiment run.
with mlflow.start_run():
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions and compute accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Save the trained model locally as a .pkl file
    joblib.dump(model, "model.pkl")

    # Log the trained model to MLflow as an artifact
    # This allows model versioning and later retrieval
    mlflow.sklearn.log_model(model, "random-forest-model")

    # Log the hyperparameter n_estimators to MLflow
    # This enables comparison between runs with different values
    mlflow.log_param("n_estimators", 200)

    # Log the accuracy metric to MLflow
    # MLflow will store this value for analysis and comparison across runs
    mlflow.log_metric("accuracy", accuracy)

    print(f"Model trained with accuracy: {accuracy:.4f}")
    print("Experiment successfully logged with MLflow.")

    # ---------------------------
    # CML REPORT
    # ---------------------------

    # Compute the confusion matrix from true and predicted labels
    cm = confusion_matrix(y_test, y_pred)

    # Create a figure to visualize the confusion matrix
    plt.figure(figsize=(8, 6))

    # Plot the confusion matrix as a heatmap
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

    # Add title and axis labels
    plt.title("Confusion Matrix")
    plt.xlabel("Predictions")
    plt.ylabel("True Values")

    # Save the figure as an image so CML can include it in the report
    plt.savefig("outputs/confusion_matrix.png")

    print("Confusion matrix saved as 'confusion_matrix.png'")
