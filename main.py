import requests

API_KEY = "ab5a8d75fd21220fa951f31619cb0371"
API_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(date):
    response = requests.get(API_URL, params={"q": "London,UK", "appid": API_KEY})
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if date in item["dt_txt"]:
                temp = item["main"]["temp"]
                print(f"Temperature on {date}: {temp:.2f}°C")
                return
        print("Date not found in the forecast.")
    else:
        print("Error fetching data from the API.")


def get_wind_speed(date):
    response = requests.get(API_URL, params={"q": "London,UK", "appid": API_KEY})
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if date in item["dt_txt"]:
                wind_speed = item["wind"]["speed"]
                print(f"Wind Speed on {date}: {wind_speed} m/s")
                return
        print("Date not found in the forecast.")
    else:
        print("Error fetching data from the API.")


def get_pressure(date):
    response = requests.get(API_URL, params={"q": "London,UK", "appid": API_KEY})
    if response.status_code == 200:
        data = response.json()
        for item in data["list"]:
            if date in item["dt_txt"]:
                pressure = item["main"]["pressure"]
                print(f"Pressure on {date}: {pressure} hPa")
                return
        print("Date not found in the forecast.")
    else:
        print("Error fetching data from the API.")


if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
            get_weather(date)
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
            get_wind_speed(date)
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss format): ")
            get_pressure(date)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
