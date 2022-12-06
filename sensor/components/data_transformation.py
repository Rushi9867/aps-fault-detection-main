from sensor.entity import artifact_entity,config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
from typing import Optional 
from sensor import utils 
import numpy as np 
from sklearn.preprocessing import LabelEncoder 


class DataTransformation:
    def __init__(self,data_transformation_config:config_entity.DataTransformationConfig,\
                 data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            self.data_transformation_config=data_transformation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
        
        def get_data_transformer_object(cls):
            try:
                simple_imputer = SimpleImputer(strategy="constant",fill_value=0)
                constant_pipeline = Pipeline(steps=[('Imputer',simple_imputer),('RobustScaler',robust_scaler)])
            except Exception as e:
                raise SensorException(e,sys)
            
        def initiate_data_transformation(self,) -> artifact_entity.DataTransformationArtifact:
            try:
                train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
                test_df = pd.read_csv(self.data_ingestion_artifact.test-file_path)
                
                input_feature_train_df = train_df[TARGET_COLUMN]
                target_feature_test_df = test_df[TARGET_COLUMN]
                
                target_feature_train_arr = label_encoder.transform(target_feature_train_df)
                target_feature_test_arr = label_encoder.transform(target_feature_test_df)
                
                transformation_pipeline = DataTransformation.get_data_transformer(input_feature_train_df)
                transformation_pipeline = DataTransformation.get_data_transformer(input_feature_test_df)
                
                smt = SMOTETomek(sampling_strategy)
                input_feature_train_arr = transformation_pipeline.transform(input_feature_train_df)
                input_feature_train_arr = transformation_pipeline.transform(input_feature_test_df)
                
                # 
                utils.save_numpy_array_data(file_path=self.data_transformation_config)
                
                logging.info(f"Data transformation")
                
            except Exception as e:
                raise SensorException(e,sys)
            
