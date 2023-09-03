import os, sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.logger import logging
import pickle

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            model_name = list(models.keys())[i]

            logging.info("Performing hyper parameter tuning for : " + model_name)

            # Perform hyper parameter tuning using grid search cv
            gs = GridSearchCV(model, param, cv = 5)
            gs.fit(X_train, y_train)

            logging.info("Hyper parameter tuning finished for : " + model_name)

            # Fit the model based on the best params found by grid search cv
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Perform predictions on test set
            y_test_pred = model.predict(X_test)

            # Find the r2 score on test set
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score

            logging.info("Model training and evaluation done for : " + model_name)
        return report
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
