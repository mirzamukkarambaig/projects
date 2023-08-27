# Azure Data Explorer Data Retriever

This project includes a Python class, ADXDataRetriever, for retrieving data from Azure Data Explorer (ADX).

## Dependencies

This project depends on the following Python packages:

- `datetime`
- `typing`
- `concurrent.futures`
- `pandas==1.3.1`
- `json`
- `logging`
- `abc`
- `time`
- `azure.kusto.data==2.10.0`

## Installation
You can install the dependencies with pip:

```bash
pip install -r requirements.txt
```


## UML

```plaintext
+---------------------------------+
|           BaseQuery             |
+---------------------------------+
| -day_str: str                   |
| -next_day_str: str              |
+---------------------------------+
| +get_query(): str               |
+---------------------------------+

+---------------------------------+
|            Query1               |
+---------------------------------+
| Inherits from BaseQuery         |
+---------------------------------+
| +get_query(): str               |
+---------------------------------+

+---------------------------------+
|            Query2               |
+---------------------------------+
| Inherits from BaseQuery         |
+---------------------------------+
| +get_query(): str               |
+---------------------------------+

... (more query classes) ...

+---------------------------------------+
|          ADXDataRetriever             |
+---------------------------------------+
| -config: dict                         |
| -query_classes: List[BaseQuery]       |
| -days: List[datetime]                 |
| -client: KustoClient                  |
+---------------------------------------+
| +__init__(...)                        |
| +read_configuration_file(): dict      |
| +create_connection()                  |
| -_update_queries(day: datetime)       |
| +execute_query(query: BaseQuery)      |
| +retrieve_data(): DataFrame           |
| +save_to_parquet_file(...)            |
+---------------------------------------+
```

## Usage

To retrieve data from Azure Data Explorer using the `ADXDataRetriever` class, follow these steps:

```python
from datetime import datetime, timedelta
from ADXDataRetriever import ADXDataRetriever, Query1, Query2
import time

# 1. Define the days for which you want to retrieve data
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 2, 1)
days = [start_date + timedelta(days=x) for x in range((end_date-start_date).days)]

# 2. Define the list of query classes
query_classes = [Query1, Query2]

# 3. Initialize the ADXDataRetriever
data_retriever = ADXDataRetriever(config_path="config.json", query_classes=query_classes, days=days)

# 4. Establish a connection to the ADX service
data_retriever.create_connection()

# 5. Retrieve the data and save it to a Parquet file
start_time = time.time()
data_retriever.save_to_parquet_file("data.parquet")
print(f"Overall Time: {time.time() - start_time} seconds")
```

Make sure to customize the `start_date`, `end_date`, and any other necessary configurations before executing the script.
## License

This project is licensed under the terms of the MIT license.