from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run-plan")
def run_plan():
    result = subprocess.run(
        ["sqlmesh", "-p", ".", "plan", "dev", "--auto-apply"],
        capture_output=True,
        text=True,
        cwd="/app",
    )
    return {
        "success": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }