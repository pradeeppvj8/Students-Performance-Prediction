import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        pass

    def initiate_train_pipeline(self):
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        logging.info("Data Ingestion is completed")

        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
        logging.info("Data transformation is completed")

        model_trainer = ModelTrainer()
        best_model_score = model_trainer.initate_model_trainer(train_arr, test_arr)

        logging.info("Model training is completed with best model score - " +str(best_model_score))

        if best_model_score and best_model_score > 0.6:
            return True
        else:
            return False 