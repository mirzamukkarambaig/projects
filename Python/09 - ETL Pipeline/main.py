# main.py
import mysql.connector
import uuid
from datetime import datetime
from config import DB_CONFIG, API_KEY, BASE_URL
from utils import fetch_data


def insert_into_db(query, values):
    with mysql.connector.connect(**DB_CONFIG) as cnx, cnx.cursor() as cursor:
        cursor.execute(query, values)
        cnx.commit()


def main():
    lat = "31.5204"
    lon = "74.3587"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }
    data = fetch_data(BASE_URL, params)
    if not data:
        return

    timestamp = datetime.utcfromtimestamp(data['list'][0]['dt']).strftime('%Y-%m-%d %H:%M:%S')

    query = "INSERT INTO locations (location_code, location_name, longitude, latitude) VALUES (%s, %s, %s, %s)"
    values = ('LHR', 'Lahore', data['coord']['lon'], data['coord']['lat'])
    insert_into_db(query, values)

    query = "INSERT INTO air_quality (aqi_uuid, location_code, aqi_value, measured_at) VALUES (%s, %s, %s, %s)"
    values = (str(uuid.uuid4()), 'LHR', data['list'][0]['main']['aqi'], timestamp)
    insert_into_db(query, values)


if __name__ == "__main__":
    main()
