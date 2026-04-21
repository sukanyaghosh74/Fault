# Fault-Tolerant REST API

## Features
- Retry mechanism with exponential backoff
- Handles unstable service failures
- Centralized logging system
- Graceful error handling
- Dockerized deployment
- CI/CD enabled

## Run locally
pip install -r requirements.txt
python app.py

## Test API
Visit: http://localhost:5000/data

## Fault Injection
The internal service randomly fails.
Retry logic ensures recovery before returning error.
