"""
Dagster assets - Example assets
"""
from dagster import asset, get_dagster_logger
import time

logger = get_dagster_logger()


@asset(group_name="examples", compute_kind="python")
def long_running_asset():
    """Example long-running asset"""
    for i in range(12):
        logger.info(f"Running batch {i+1}/12...")
        time.sleep(3)
    logger.info("✅ long_running_asset completed.")


@asset(group_name="examples", compute_kind="python")
def simple_asset():
    """Example simple asset"""
    logger.info("✅ simple_asset completed.")
    return "simple_asset"


@asset(group_name="examples", compute_kind="python", deps=[simple_asset])
def another_simple_asset():
    """Example asset with dependency"""
    logger.info("✅ another_simple_asset completed.")
    return "another_simple_asset"
