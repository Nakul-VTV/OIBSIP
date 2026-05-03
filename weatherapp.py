import requests
import os
API_KEY = os.getenv("WEATHER_API_KEY")
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print("Error:", data.get("message", "Unable to fetch weather"))
            return
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    except requests.exceptions.RequestException:
        print("Network error. Please check your connection.")
def main():
    city = input("Enter city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return
    get_weather(city)
if __name__ == "__main__":
    main()
