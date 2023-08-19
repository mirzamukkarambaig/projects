from datetime import datetime, timedelta
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from azure.kusto.data.helpers import dataframe_from_result_table
import pandas as pd
import json
import logging
from abc import ABC, abstractmethod
import time

# Set up logging
logging.basicConfig(filename='my_log_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
PARQUET_PATH = "data.parquet"
CONFIG_PATH = "config.json"

class BaseQuery(ABC):
    def __init__(self, day_str, next_day_str):
        self.day_str = day_str
        self.next_day_str = next_day_str

    @abstractmethod
    def get_query(self):
        pass


class Query1(BaseQuery):
    def get_query(self):
        return f"... Your Query for retireving data {self.day_str} to {self.next_day_str}"


class Query2(BaseQuery):
    def get_query(self):
        return f"... Your Query for retireving data {self.day_str} to {self.next_day_str}"

# ... here goes the rest of your queries ...

class ADXDataRetriever:
    """
    A class used to retrieve data from Azure Data Explorer (ADX) for a range of days.
    """

    @staticmethod
    def read_configuration_file(file_path: str) -> dict:
        """
        Read a JSON configuration file.
        """
        try:
            with open(file_path, "r") as f:
                config = json.load(f)
        except FileNotFoundError:
            logging.error(f"Configuration file not found: {file_path}")
            return {}
        except json.JSONDecodeError:
            logging.error(f"Failed to decode JSON from configuration file: {file_path}")
            return {}

        return config

    def __init__(self, config_path: str = CONFIG_PATH, query_classes: List[BaseQuery] = [], days: List[datetime] = []):
        """
        Constructs all the necessary attributes for the ADXDataRetriever object.
        """
        print("Constructor Initializing...")
        self.config = self.read_configuration_file(config_path)

        if not self.config:
            raise ValueError(f"Invalid configuration data in file {config_path}")

        self.query_classes = query_classes
        self.days = days
        self.client = None  # Connection will be established later

    def create_connection(self):
        """
        Establishes connection to the ADX service and assigns it to self.client.
        """
        try:
            print("Creating Connection...")
            kcsb = KustoConnectionStringBuilder.with_aad_application_key_authentication(
                self.config['adx_connection_string']['cluster'],
                self.config['adx_connection_string']['client_id'],
                self.config['adx_connection_string']['client_secret'],
                self.config['adx_connection_string']['authority_id']
            )
            self.client = KustoClient(kcsb)
        except Exception as e:
            logging.error(f"Failed to create connection: {str(e)}")
            raise

    def _update_queries(self, day: datetime) -> List[BaseQuery]:
        """
        Updates the queries for the given day and returns the updated queries.
        """
        print("Updating Queries...")
        day_str = day.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        next_day_str = (day + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S") + "Z"

        return [query_class(day_str, next_day_str) for query_class in self.query_classes]

    def execute_query(self, query: BaseQuery) -> Optional[pd.DataFrame]:
        """
        Executes ADX query and returns the result as a pandas DataFrame.
        """
        if self.client is None:
            logging.error("Client is not connected")
            return None

        try:
            print("Executing Query...")
            response = self.client.execute(self.config['adx_connection_string']['database'], query.get_query())
            df = dataframe_from_result_table(response.primary_results[0])
            return df
        except Exception as e:
            logging.error(f"Query execution failed: {str(e)}")
            return None

    def retrieve_data(self) -> Optional[pd.DataFrame]:
        """
        Retrieves data for the specified days by executing multiple queries in parallel and concatenating the results.
        """
        if not self.days or not self.query_classes:
            logging.error("Days or query classes are not specified")
            return None

        dataframes = []
        for day in self.days:
            print(f"Working on {day}...")
            updated_queries = self._update_queries(day)

            # Use a ThreadPoolExecutor to run the queries in parallel
            with ThreadPoolExecutor(max_workers=min(10, len(updated_queries))) as executor:
                day_dataframes = list(executor.map(self.execute_query, updated_queries))

            # If any query execution failed, we skip that query's result
            day_dataframes = [df for df in day_dataframes if df is not None]

            # Concatenate the resulting dataframes
            if day_dataframes:  # Check if there are dataframes to concatenate
                day_df = pd.concat(day_dataframes, axis=0)
                dataframes.append(day_df)

        # Concatenate the dataframes for all days
        if dataframes:  # Check if there are dataframes to concatenate
            df = pd.concat(dataframes)
            return df

        logging.error("All query executions failed")
        return None

    def save_to_parquet_file(self, file_path: str, partition_cols: Optional[List[str]] = None, compression: str = 'snappy'):
        """
        Retrieves the data and saves it to a Parquet file.
        """
        try:
            print("Trying to Save in the Parquet file...")
            df = self.retrieve_data()

            if df is None:
                logging.error("No data retrieved")
                return

            if df.empty:
                logging.error("Data retrieved is empty")
                return

            df.to_parquet(file_path, partition_cols=partition_cols, compression=compression)
        except Exception as e:
            logging.error(f"Failed to save data to Parquet file: {str(e)}")

# ---------------------------------Main Function---------------------------------#

if __name__ = "__main__":
    
    # 1. Create a list of days
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 2, 1)
    days = [start_date + timedelta(days=x) for x in range((end_date-start_date).days)]
    
    # 2. Create a list of query classes
    query_classes = [Query1, Query2] 
    
    # 3. Create an instance of ADXDataRetriever
    data_retriever = ADXDataRetriever(config_path=CONFIG_PATH, query_classes=query_classes, days=days)
    
    # 4. Establish a connection
    data_retriever.create_connection()
    
    # 5. Retrieve the data and save it to a Parquet file
    start_time = time.time()
    data_retriever.save_to_parquet_file(PARQUET_PATH)
    print(f"Overall Time: {time.time() - start_time} seconds")
