import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "effe5e12eab2fa1c39a7e51342d33acf"

def main():
    # Get the city name from user
    City = get_city_name()

    # Get the weather data from OpenWeatherMap API
    response = get_weather_data(City)

    # Get the temperature in Kelvin from response
    temp_kelvin = response['main']['temp']

    # Convert the temperature from Kelvin to Celsius and Fahrenheit
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    
    # Get the feels like temperature in Kelvin from response
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    
    # Get the humidity from response
    humidity = response['main']['humidity']
    
    #Get the description from response
    description = response['weather'][0]['description']
    
    # Get the sunrise time from response and convert it to local time in hh:mm:ss format
    sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'], dt.timezone.utc)
    
    # Get the sunset time from response and convert it to local time 
    sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'], dt.timezone.utc)
    
    # Get the wind speed from response
    wind_speed = response['wind']['speed']
    
    # Get the wind direction from response
    wind_deg = response['wind']['deg']
    wind_dir = deg_to_cardinal(wind_deg)
    
    # Get the pressure from response
    pressure = response['main']['pressure']
    
    # Print every information
    print(f"Temperature: {temp_celsius:.2f}°C, {temp_fahrenheit:.2f}°F")
    print(f"Feels like: {feels_like_celsius:.2f}°C, {feels_like_fahrenheit:.2f}°F")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")
    print(f"Sunrise: {sunrise_time}")
    print(f"Sunset: {sunset_time}")
    print(f"Wind speed: {wind_speed} m/s")
    print(f"Wind direction: {wind_deg}° ({wind_dir})") 
    print(f"Pressure: {pressure} hPa")

def get_weather_data(city):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()
    return response

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def deg_to_cardinal(deg):
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    idx = int((deg / 22.5) + 0.5) % 16
    return directions[idx]

def get_city_name():
    city = input("Enter the city name: ")
    return city
  
if __name__ == "__main__":
    main()