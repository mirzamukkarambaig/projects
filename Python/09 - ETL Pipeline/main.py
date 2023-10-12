import requests

lat = "31.5204"
lon = "74.3587"
api_key = "0fad45e0d18b4dd497f079a8ae4a369f"

url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)
data = response.json()

print(data)
