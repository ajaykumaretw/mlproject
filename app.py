from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
if __name__=="__main__":
    logging.info("Execution has started")
    
    try:
     1/0
    except Exception as e:
     logging.info("Project custom exception")
     raise CustomException(e,sys) 
