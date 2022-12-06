import os,sys
from sensor.exception import SensorException
from sensor.logger import logging 
from datetime import datetime 
FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME  = "test.csv"

class TrainingPipelineConfig:
    def __init__(self):
        self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strtime('%m%d%Y__%H%M%S')}")
    
class DataIngestionConfig:
    def __init__(self,training_Pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name = "aps"
            self.collection_name = "sensor"
            self.data_ingestion_dir = os.path.join(training_Pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_dir = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise SensorException(e,sys)
    def to_dict()->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)
            
        
class DataValidatioConfig:
    
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.Data_validatio_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
        self.report_file_path =os.path.join(self.Data_validatio_dir,"report.yaml")
        self.missing_threshold:float=0.2
        self.base_file_path =os.path.join("D:/Python Programs/Machine Learning/Projects/aps-fault-detection-main/aps_failure_training_set1.csv")
        
class DataTransformationConfig:
    self.data_transformation_dir = os.path.join(training_pipeline_config)
    self.transform_object_path = os.path.join(data_transformation_dir)
    self.transformed_train_path = o.path.join(data_transformation_dir)
    self.transformed_test_path = os.path.join()
    self.target_encoder_path = os.path.join()
    
    
class ModelTrainingConfig:...
class ModelEvaluationConfig:... 
class ModelPusherConfig:...