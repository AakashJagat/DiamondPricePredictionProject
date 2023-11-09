from src.DiamondPricePrediction.components.data_ingestion import DataIngestion

import os
import sys
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import customexception
import pandas as pd
import numpy  as np

obj = DataIngestion()

obj.initiate_data_ingestion()