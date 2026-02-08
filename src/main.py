from fastapi import FastAPI
import os

app = FastAPI(title="PipeCD GitOps Demo")

# Get version from environment variable (set in Dockerfile/K8s)
APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Hello from PipeCD-managed EKS!",
        "version": APP_VERSION
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    # Placeholder for Prometheus/CloudWatch metrics
    return {"uptime": "100%", "requests": 0}