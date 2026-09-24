import subprocess
from dagster import asset, Definitions

@asset
def sqlmesh_test_model():
    result = subprocess.run(
        ["sqlmesh", "-p", "sqlmesh", "plan", "dev", "--auto-apply"],
        capture_output=True,
        text=True,
        cwd="/Users/Dmytro_Bukanov/Desktop/data-tests",
    )
    print(result.stdout)
    if result.returncode != 0:
        raise Exception(f"SQLMesh failed: {result.stderr}")

defs = Definitions(
    assets=[sqlmesh_test_model],
)