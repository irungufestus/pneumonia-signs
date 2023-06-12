import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/evaluation.py",
    f"src/components/prepare_base_model.py",
    f"src/components/prepare_callbacks.py",
    f"src/components/training.py",
    f"src/components/data_predict.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/exception.py",
    f"src/pipeline/predict.py",
    f"src/pipeline/stage01_dataIngestion.py",
    f"src/pipeline/stage02_prepare_base_model.py",
    f"src/pipeline/stage03_training.py",
    f"src/pipeline/stage04_evaluation.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    f"src/logger.py",
    f"src/customException.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",    
    f"src/entity/__init__.py",
    f"src/entity/config_entity.py",
    f"src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    f"artifacts/",
    "research/trials.ipynb",
    "templates/index.html"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")