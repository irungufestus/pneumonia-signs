import os
import sys
from  dataclasses import dataclass
from src.pipeline import logger
from src.pipeline import CustomException
from src.pipeline.utils import save_object
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.training import Training
from cnnClassifier import logger



STAGE_NAME = "Model Training"
@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path

@dataclass
class modelTrainingConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")
class  modelTrainer:
    def __init__(self ):
        self.modelTrainerConfig=modelTrainingConfig()
    def initiate_model_trainer(self):
        self.get_base_model()
        self.train_valid_generator()
        self.train( callback_list=callback_list)
@dataclass        
class callbacks_config:
    def _init_(self):
        self.callbacks_config=callbacks_config()
    def prepare_callbacks_config(self):
        self.get_tb_ckpt_callbacks() 
        
        
      
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()


        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e