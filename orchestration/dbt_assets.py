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
