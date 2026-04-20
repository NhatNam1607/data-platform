from pathlib import Path
from dagster import Definitions

from .assets import all_assets
from .schedules import dbt_daily_schedule
from .resources import get_dbt_resource

# dbt project path
DBT_PROJECT_DIR = Path(__file__).parent.parent / "transformation"

defs = Definitions(
    assets=all_assets,
    schedules=[dbt_daily_schedule],
    resources={
        "dbt": get_dbt_resource(DBT_PROJECT_DIR, target="dev"),
    },
)
