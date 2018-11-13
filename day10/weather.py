import requests

data = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Glasgow,uk&appid=052f26926ae9784c2d677ca7bc5dec98&units=metric')

# Command-d or control-d: finds next occurence of highlight word.
weather_data = data.json()

# Display the current temperature, the high and low temperate, the current weather description, and the name of the city that came back from the API.

temperature = weather_data["main"]["temp"]
min_temperature = weather_data["main"]["temp_min"]
max_temperature = weather_data["main"]["temp_max"]

weather = weather_data["weather"][0]["main"]
weather_description = weather_data["weather"][0]["description"]

city_name = weather_data["name"]

print("The weather in", city_name, "is", weather, "-", weather_description)
print("The current temperature is", temperature,
      "with a low of", min_temperature,
      "and a high of", max_temperature)

# def celsius_to_fahrenheit(c):
#     return ...
