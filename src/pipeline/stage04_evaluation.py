from src.config.configuration import ConfigurationManager
from  src.components.evaluation import Evaluation
from src import logger ,CustomException
import sys




STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()

if __name__ == " _main_":
    try:
        logger.info(f"stage {STAGE_NAME} has started")
        obj=EvaluationPipeline()
        obj.main
        logger.info(f"stage {STAGE_NAME} has started")
        
    except Exception as e:
        raise CustomException(e, sys)

