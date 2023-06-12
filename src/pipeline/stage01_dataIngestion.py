from src.pipeline import logger,CustomException
from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
import sys

STAGE_NAME="Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        
if __name__ == " _main_":
    try:
        logger.info(f"stage {STAGE_NAME} has started")
        obj=DataIngestionTrainingPipeline()
        obj.main
        logger.info(f"stage {STAGE_NAME} has started")
        
    except Exception as e:
        raise CustomException(e, sys)
    


    
    