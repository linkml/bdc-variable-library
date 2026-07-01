"""bdc-variable-library.

LinkML models for variables in the BDC Knowledge Library
"""

try:
    from bdc_variable_library._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
