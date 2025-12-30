import requests

def get_weather(location, api_key):
    # Base URL for OpenWeatherMap Current Weather API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    # 'q' handles city names or ZIP codes
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            city = data["name"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]

            print(f"\n--- Weather in {city} ---")
            print(f"Condition: {condition.capitalize()}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data.get('message', 'Could not retrieve data.')}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY_HERE' with your actual OpenWeatherMap API key
    MY_API_KEY = "5d967a5d2c9ccb14fadb8be0d9fa91e1"
    
    user_input = input("Enter a city name or ZIP code: ")
    get_weather(user_input, MY_API_KEY)