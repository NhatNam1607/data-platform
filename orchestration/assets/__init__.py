"""
Assets module - All Dagster assets organized by layer
"""
from dagster import load_assets_from_modules

from . import transformation

# Load all assets from submodules
all_assets = load_assets_from_modules([transformation])

__all__ = ["all_assets"]
