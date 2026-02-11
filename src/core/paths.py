import sys
from pathlib import Path


def get_base_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent

    return Path(__file__).resolve().parents[2]


def get_data_dir() -> Path:
    path = get_base_dir() / "data"
    path.mkdir(exist_ok=True)
    return path


def get_output_dir() -> Path:
    path = get_base_dir() / "output"
    path.mkdir(exist_ok=True)
    return path


def get_template_dir() -> Path:
    path = get_base_dir() / "template"
    path.mkdir(exist_ok=True)
    return path
