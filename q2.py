import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_temperature_by_date(date_time):
    response = requests.get(API_URL)
    print(response)
    
    data = response.json()
    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['main']['temp']

def get_wind_speed_by_date(date_time):
    response = requests.get(API_URL)
    data = response.json()
    

    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['wind']['speed']

def get_pressure_by_date(date_time):
    response = requests.get(API_URL)
    data = response.json()
    for entry in data['list']:
        if entry['dt_txt'] == date_time:
            return entry['main']['pressure']

while True:
    print("Menu:")
    print("1. Get Temperature")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        date_time = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
        temperature = get_temperature_by_date(date_time)
        print(f"Temperature at {date_time}: {temperature}°C")

    elif choice == '2':
        date_time = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
        wind_speed = get_wind_speed_by_date(date_time)
        print(f"Wind Speed at {date_time}: {wind_speed} m/s")

    elif choice == '3':
        date_time = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
        pressure = get_pressure_by_date(date_time)
        print(f"Pressure at {date_time}: {pressure} hPa")

    elif choice == '0':
        break

    else:
        print("Invalid choice. Please try again.")

print("Program terminated.")