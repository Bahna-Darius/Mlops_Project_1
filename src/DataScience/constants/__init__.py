from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent.parent

CONFIG_FILE_PATH = BASE_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"
SCHEMA_FILE_PATH = ROOT_DIR / "schema.yaml"
