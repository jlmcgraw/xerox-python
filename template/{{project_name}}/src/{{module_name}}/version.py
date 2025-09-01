"""docstring TBD."""
from importlib import metadata
import tomllib


def get_version_from_metadata() -> str:
    """Return the version from metadata."""
    return metadata.version(__package__ or __name__)


def get_version_from_pyproject() -> str:
    """Return the version from pyproject.toml."""
    with open("pyproject.toml", "rb") as file:
        return str(tomllib.load(file)["project"]["version"])


def get_version() -> str:
    """Return the version from metadata or pyproject.toml."""
    try:
        return get_version_from_metadata()
    except metadata.PackageNotFoundError:
        try:
            return get_version_from_pyproject()
        except (FileNotFoundError, KeyError):
            return "unknown"


__version__ = get_version()
