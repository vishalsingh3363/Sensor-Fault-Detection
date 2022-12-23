from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
#from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.utils.main_utils import read_yaml_file

def set_env_variable(env_file_path):
    env_config= read_yaml_file(env_file_path)
    os.environ['MONGO_DB_URL']= env_config['MONGO_DB_URL']

if __name__ == '__main__':
    try:
        env_file_path='/config/workspace/env.yaml'
        set_env_variable(env_file_path)
        training_pipeline=TrainPipeline()
        training_pipeline.run_pipeline()
        #training_pipeline= TrainPipeline()
        #training_pipeline.run_pipeline()
        #training_pipeline_config= TrainingPipelineConfig()
        #data_ingestion_config= DataIngestionConfig(training_pipeline_config= training_pipeline_config)
        #print(data_ingestion_config.__dict__)

        #mongodb_client = MongoDBClient()
        #print("collection name:",mongodb_client.database.list_collection_names())
    except Exception as e:
        print(e)
        logging.exception(e)