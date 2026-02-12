import os
import mlflow

def train():
    mlflow.start_run()
    mlflow.log_param("pipeline", "dvc-run")
    mlflow.log_metric("accuracy", 0.88)
    mlflow.end_run()

    # Ensure models directory exists
    os.makedirs("models", exist_ok=True)

    # Create dummy model file
    with open("models/model.txt", "w") as f:
        f.write("dummy model content")

if __name__ == "__main__":
    train()
