import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "text_summarizer_app"


list_of_files = [
    ".github/workflows/.gitkeep",                      # CI/CD YAML file
    f"src/{project_name}/__init__.py",                     
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/thompson_sampling.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction.py",
    "app.py",
    "main.py",
    "dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "README.md"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok = True)
        logging.info(f"Creating directory {file_dir} for file {file_name}")


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"Creating empty file {file_path}")
    else:
        logging.info(f"{file_path} file already exists")
