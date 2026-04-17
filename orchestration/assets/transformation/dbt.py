"""
dbt assets - Integration with dbt models
"""
from pathlib import Path
from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets, DbtProject

# dbt project path (go up 3 levels: dbt.py -> transformation -> assets -> orchestration -> root)
DBT_PROJECT_DIR = Path(__file__).parent.parent.parent.parent / "transformation"

# Load dbt project
dbt_project = DbtProject(
    project_dir=DBT_PROJECT_DIR,
    packaged_project_dir=DBT_PROJECT_DIR,
)

# Prepare manifest if not exists
# Note: prepare_if_dev() only works when DAGSTER_IS_DEV_CLI=1 (dagster dev command)
# In Docker, we use dagster api grpc, so we call prepare() explicitly
if not dbt_project.manifest_path.exists():
    dbt_project.preparer.prepare(dbt_project)


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
