"""
dbt assets - Integration with dbt models
"""
from pathlib import Path
from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets, DbtProject

# dbt project path
DBT_PROJECT_DIR = Path(__file__).parent.parent / "transformation"

# Load dbt project
dbt_project = DbtProject(
    project_dir=DBT_PROJECT_DIR,
    packaged_project_dir=DBT_PROJECT_DIR,
)

# Prepare manifest
print(f"[DEBUG] Checking manifest at: {dbt_project.manifest_path}")
print(f"[DEBUG] Manifest exists: {dbt_project.manifest_path.exists()}")

try:
    dbt_project.prepare_if_dev()
    print(f"[DEBUG] prepare_if_dev() completed successfully")
    print(f"[DEBUG] Manifest exists after prepare: {dbt_project.manifest_path.exists()}")
except Exception as e:
    print(f"[ERROR] prepare_if_dev() failed: {e}")
    import traceback
    traceback.print_exc()


@dbt_assets(
    manifest=dbt_project.manifest_path,
    project=dbt_project,
)
def transformation_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    """
    All dbt models as Dagster assets
    
    Dagster will:
    - Understand dependencies between models
    - Visualize lineage graph
    - Track asset materializations
    - Schedule runs
    """
    yield from dbt.cli(["build"], context=context).stream()
