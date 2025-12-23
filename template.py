import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(message)s]"
)

while True:
    project_name=input("Enter your project name: ")

    if project_name.strip() !="":
        break
    else:
        logging.info("Prject name can not be empty, Please try again")


logging.info(f"Creating Project {project_name}")

#list of files:
list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    print(filepath)