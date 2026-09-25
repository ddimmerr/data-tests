import requests
from dagster import asset, Definitions

@asset
def sqlmesh_test_model():
    response = requests.post("http://localhost:8000/run-plan")
    data = response.json()
    if not data["success"]:
        raise Exception(f"SQLMesh failed: {data['stderr']}")
    print(data["stdout"])

defs = Definitions(
    assets=[sqlmesh_test_model],
)