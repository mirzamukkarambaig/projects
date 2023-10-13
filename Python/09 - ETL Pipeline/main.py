import requests
import mysql.connector
import uuid
from datetime import datetime

# Extraction
lat = "31.5204"
lon = "74.3587"
api_key = "0fad45e0d18b4dd497f079a8ae4a369f"

url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data)

# Transformation and Loading
timestamp = datetime.utcfromtimestamp(data['list'][0]['dt']).strftime('%Y-%m-%d %H:%M:%S')

# Database Connection
config = {
    'user': 'root',
    'password': '*csy!@FPT6o5HT8Q#2',
    'host': 'localhost',
    'database': 'AirQualityDB',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

# Create a cursor
cursor = cnx.cursor()

query = "INSERT INTO locations (location_code, location_name, longitude, latitude) VALUES (%s, %s, %s, %s)"
values = ('LHR', 'Lahore', data['coord']['lon'], data['coord']['lat'])
cursor.execute(query, values)
cnx.commit()

query = "INSERT INTO air_quality (aqi_uuid, location_code, aqi_value, measured_at) VALUES (%s, %s, %s, %s)"
values = (str(uuid.uuid4()), 'LHR', data['list'][0]['main']['aqi'], timestamp)
cursor.execute(query, values)
cnx.commit()

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cursor.close()
cnx.close()
