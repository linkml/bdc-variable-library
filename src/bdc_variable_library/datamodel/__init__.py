"""Data model package for bdc-variable-library."""

from pathlib import Path
from .bdc_variable_library import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "bdc_variable_library.yaml"
