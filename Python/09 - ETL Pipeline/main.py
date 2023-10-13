import requests
import pandas as pd
import mysql.connector

lat = "31.5204"
lon = "74.3587"
api_key = "0fad45e0d18b4dd497f079a8ae4a369f"

url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data)

# Extract components from the data
components = data['list'][0]['components']

# Convert the dictionary to a DataFrame
df = pd.DataFrame(list(components.items()), columns=['Component', 'Concentration'])

print(df)

config = {
    'user': 'root',
    'password': '*csy!@FPT6o5HT8Q#2',
    'host': 'localhost',
    'database': 'air_pollution',
    'raise_on_warnings': True
}

# Connect to the database
cnx = mysql.connector.connect(**config)

# Create a cursor
cursor = cnx.cursor()

# Insert DataFrame records one by one.
for i, row in df.iterrows():
    sql = "INSERT INTO concentration (component_id, value) VALUES (%s, %s)"
    values = (row['Component'], row['Concentration'])  # Assuming column names in df are 'Component' and 'Concentration'
    cursor.execute(sql, values)

# Commit the inserts
cnx.commit()

# Print concentration table
cursor.execute("SELECT * FROM concentration")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cursor.close()
cnx.close()
