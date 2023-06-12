import os
import sys
import yaml
from ensure import ensure_annotations
from pathlib import Path
from src.exception import CustomException
from src import logger
from typing import Any
import base64
import numpy as np 
import pandas as pd
#import dill
import pickle


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def read_yaml(path_to_yaml:Path):
    """reads yaml file and returns
    
    Keyword arguments:
    argument -- path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        dict, The read yaml object
    """
    if not os.path.exists(path_to_yaml):
        raise logger.info(f" Cannot read '%s'. Parent dir '%s' does not exist  {path_to_yaml}")
    file_path = os.path.join( path_to_yaml)
    if not os.exists(file_path):
        raise logger.info(f" yaml_file {file_path} does not exist.")    
    try:
        with open(file_path, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file,Path)
            logger.info(f" yaml_file {path_to_yaml}loaded sucessfully")
        return (content)
                    
    except Exception as e:
        raise  CustomException(e,sys)

        

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    