"""
Dagster Application - Entry point
"""
from pathlib import Path
from dagster import Definitions, load_assets_from_modules
from dagster_dbt import DbtCliResource

from . import assets, dbt_assets
from .schedules import dbt_daily_schedule

# Load all assets
all_assets = load_assets_from_modules([assets, dbt_assets])

# dbt project path
DBT_PROJECT_DIR = Path(__file__).parent.parent / "transformation"

defs = Definitions(
    assets=all_assets,
    schedules=[dbt_daily_schedule],
    resources={
        "dbt": DbtCliResource(
            project_dir=str(DBT_PROJECT_DIR),
            profiles_dir=str(DBT_PROJECT_DIR),
            target="dev",
        ),
    },
)
