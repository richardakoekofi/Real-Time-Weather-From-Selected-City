import requests
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv

load_dotenv()
# store your api key in .env file
API_KEY = os.getenv("API_KEY")

# This function generates latitude and longitude of the city which will then be used by the API.
def lat_lon(city_name):

    geolocator = Nominatim(user_agent="weather_app")

    location = geolocator.geocode(city_name)

    if location:
        return location.latitude, location.longitude

    return None, None

# Main function to get weather from Open Weather API
def get_weather(city_name):

    lat, lon = lat_lon(city_name)

    if lat is None:
        return None, 404

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    return response.json(), response.status_code


city_name = input("Enter city name: ")

data, status = get_weather(city_name)

if status == 200:

    print("\n===== WEATHER REPORT =====")

    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['main']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

else:
    print("Error fetching weather data.")
