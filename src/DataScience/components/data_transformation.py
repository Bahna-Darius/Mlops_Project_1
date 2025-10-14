from datascience import logger_app
from sklearn.model_selection import train_test_split
from datascience.entity.config_entity import DataTransformationConfig
import pandas as pd
import os


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        # Note: Can add different data transformation techniques such as Scaler, PCA and all

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        # Split the data (0.75, 0.25)
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger_app.info("Split data into training and test sets")
        logger_app.info(train.shape)
        logger_app.info(test.shape)

        print(train.shape)
        print(test.shape)

