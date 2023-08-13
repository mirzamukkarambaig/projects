# Azure Data Explorer Data Retriever

This project includes a Python class, ADXDataRetriever, for retrieving data from Azure Data Explorer (ADX).

## Dependencies

This project depends on the following Python packages:

- pandas==1.3.1
- azure-kusto-data==2.10.0

The exact versions of these dependencies that are known to be compatible are listed in the requirements.txt file.

## Installation
You can install the dependencies with pip:

```bash
pip install -r requirements.txt
```

## UML
```plaintext
+---------------------------------------+
|          ADXDataRetriever             |
+---------------------------------------+
| -cluster: str                         |
| -client_id: str                       |
| -client_secret: str                   |
| -authority_id: str                    |
| -database: str                        |
| -queries: List[str]                   |
| -days: List[datetime]                 |
| -client: KustoClient                  |
+---------------------------------------+
| +__init__(...)                        |
| +create_connection()                  |
| -_update_queries(day: datetime)       |
| +execute_query(query: str): DataFrame |
| +retrieve_data(): DataFrame           |
+---------------------------------------+
```

## Usage
You can use the ADXDataRetriever class to retrieve data from ADX like so:

```python
from ADXDataRetriever import ADXDataRetriever
from datetime import datetime

# Initialize the ADXDataRetriever
adx = ADXDataRetriever(
    cluster="Your cluster",
    client_id="Your client id",
    client_secret="Your client secret",
    authority_id="Your authority id",
    database="Your database",
    queries=[
        "Your Query1 using {day_str} and {next_day_str}",
        "Your Query2 using {day_str} and {next_day_str}"
    ],
    days=[datetime(2023, 1, 1)]  # add the days for which you want to retrieve data
)

# Create connection to the ADX service
adx.create_connection()

# Retrieve data for the specified days
df = adx.retrieve_data()

# df now contains the data retrieved from ADX
```

You just need to replace "Your cluster", "Your client id", "Your client secret", "Your authority id", "Your database", and the queries with your actual values.

The retrieve_data method retrieves data for the specified days by executing all queries in parallel and concatenating the results. Each query should be a string that includes {day_str} and {next_day_str} as placeholders for the start and end of the day, respectively. These placeholders will be replaced with the actual times when the method is called.

## License

This project is licensed under the terms of the MIT license.

Please customize the above template as necessary to suit your project. For instance, you may want to add sections on contributing, testing, and so on, or you may want to provide more detailed usage examples. Be sure to replace the placeholder values in the "Usage" section with your actual values.
