# DevOps Lab Project

## Project Description
This is a Python-based application demonstrating DevOps practices including:
- Docker containerization
- GitHub Actions CI pipeline
- Logging and Email alerts
- Secure environment variables using .env

## How to Run Locally

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

## How to Run with Docker

docker build -t devops-app .
docker run --env-file .env devops-app

## Tools Used
- Python
- Git
- GitHub Actions
- Docker
- Logging
- SMTP Email Alerts
