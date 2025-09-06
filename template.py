from pathlib import Path
import os
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name = "DataScience"


list_of_files = [
    ".gthub/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]

exist_file_control = 0

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if os.path.exists(filepath):
        exist_file_control += 1
    else:
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory {filedir} for the file: {filename}")

        with open(filepath,"w") as f:
            logging.info(f"Creating empty file: {filepath}")


if exist_file_control == len(list_of_files):
    logging.info("Structure has already been created!")

