# Dagster + SQLMesh Local Setup

A local proof-of-concept pipeline combining **SQLMesh** (data transformation) and **Dagster** (orchestration), with SQLMesh exposed via a small HTTP API so the two can run as fully independent, separately deployable services.

## Prerequisites

- **Python 3.12** (required — newer/older versions have dependency conflicts with some packages used here)
- **Docker Desktop**
- **Google Cloud SDK** (`gcloud` CLI)
- A GCP project with the **BigQuery API** enabled

## 1. Authenticate with GCP

>bash
>gcloud auth login
>gcloud auth application-default login --no-launch-browser
>gcloud config set project your-gcp-project-id

## 2. Set up Python environment

>python3.12 -m venv .venv
>source .venv/bin/activate
## 3. Build and run the SQLMesh container

>cd sqlmesh
>docker build -t sqlmesh-project:latest .

>docker run --rm -p 8000:8000 \
>  -v ~/.config/gcloud:/root/.config/gcloud \
>  sqlmesh-project:latest
Leave this running. Verify it's healthy in another terminal:
>curl http://localhost:8000/health
>curl -X POST http://localhost:8000/run-plan
You should get back a JSON response with "success": true.

## 4. Run Dagster locally

In a new terminal, from the project root:
>cd data-tests
>source .venv/bin/activate
>pip install -r dagster/requirements.txt
>dagster dev -f dagster/definitions.py
Open the Dagster UI at http://localhost:3000.

## 5. Materialize the asset

Go to the Assets tab
Select sqlmesh_test_model
Click Materialize
This triggers Dagster to call the SQLMesh container's /run-plan endpoint over HTTP, which runs sqlmesh plan dev --auto-apply and applies the model to BigQuery.

# Notes

SQLMesh and Dagster are fully decoupled — no shared filesystem or Python environment. Dagster only ever talks to SQLMesh over HTTP.
Right now Dagster (running on your host machine) reaches the SQLMesh container via localhost:8000, since the container's port is mapped to your host. Once this setup moves to Docker Compose, the address will change to http://sqlmesh-service:8000, using Compose's internal service DNS instead.

Credentials are mounted from your local ~/.config/gcloud directory — no keys are baked into the image.