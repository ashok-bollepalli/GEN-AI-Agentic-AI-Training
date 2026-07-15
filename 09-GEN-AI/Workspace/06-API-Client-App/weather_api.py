import requests

city = "Hyderabad"

url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": city,
    "count": 1,
    "language": "en",
    "format": "json"
}

response = requests.get(url, params = params)

json_data = response.json()

print(json_data)

latitude = 17.3616
longitude = 78.4747

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "auto"
}

response = requests.get(url, params=params, timeout=10)
weather_data = response.json()
print(weather_data["current"])