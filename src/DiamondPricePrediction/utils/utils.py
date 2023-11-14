import os
import logging
import pickle
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.components.data_ingestion import DataIngestion
from src.DiamondPricePrediction.exception import customexception

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)


    except Exception as e:
        raise customexception(e, sys)
    

def evaluate_model(X_train, y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]

            # Train model
            model.fit(X_train,y_train)


            # Predict Testing Data
            y_test_pred = model.predict(X_test)

            # Get R2 Scores for Train and Test Data
            # Train_Model_Score = R2_score(y_train, y_train_pred)
            test_model_score =r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        logging.info('Exception occured during Model Training Stage')
        raise customexception(e,sys)
    

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info('Exception occured in load_object function utils')
        raise customexception(e, sys)

