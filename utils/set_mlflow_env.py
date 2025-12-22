import os

# Set the environment variables required for MLflow + Dagshub
os.environ["MLFLOW_TRACKING_URI"] = (
    "https://dagshub.com/TUUSUARIO/mlops-practica-icai.mlflow"
)
os.environ["MLFLOW_TRACKING_USERNAME"] = "TUUSUARIO"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "TUTOKEN"

print("MLflow environment variables have been set successfully.")
