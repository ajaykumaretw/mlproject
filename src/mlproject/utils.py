import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import numpy as np
import pyodbc
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
       # Establish the connection
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={host};DATABASE={db};UID={user};PWD={password};TrustServerCertificate=yes'
        )
        logging.info("Connection Established",conn)
        df=pd.read_sql_query('Select * from persons',conn)
        print(df.head())

        return df



    except Exception as ex:
        raise CustomException(ex)
    
