"""
dbt resource configuration
"""
from pathlib import Path
from dagster_dbt import DbtCliResource


def get_dbt_resource(project_dir: Path, target: str = "dev") -> DbtCliResource:
    """
    Get configured dbt resource
    
    Args:
        project_dir: Path to dbt project directory
        target: dbt target (dev, prod, etc.)
    
    Returns:
        Configured DbtCliResource
    """
    return DbtCliResource(
        project_dir=str(project_dir),
        profiles_dir=str(project_dir),
        target=target,
    )
