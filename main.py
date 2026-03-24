print("Welcome to the Weather App!")
input("Enter any letter to start: ")

def settings_menu():
    while True:
        print("\nSettings Menu")
        print("1. Change Timezone")
        print("2. Erase Favourited City's")
        print("3. Erase Saved City's")
        print("4. Unit Of Measurements")
        print("5. Back To Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Changing timezone...")  # Replace with real function later
        elif choice == "2":
            print("Erasing favourited cities...")  # Replace with real function later
        elif choice == "3":
            print("Erasing saved cities...")  # Replace with real function later
        elif choice == "4":
            print("Changing units...")  # Replace with real function later
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


from functions import get_city_info

def main():
    while True:
        print("\nWeather App Menu:")
        print("1. Search city")
        print("2. Saved City's")
        print("3. Favourite City's")
        print("4. Settings")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter city: ")
            print(f"Searching for {name}'s details...")
            city_info = get_city_info(name)
            if city_info:
                cit = (f"City: {city_info['location']['name']}")
                cou = (f"Country: {city_info['location']['country']}")
                lat = (f"Latitude: {city_info['location']['lat']}")
                lon = (f"Longitude: {city_info['location']['lon']}")
                localtime = (f"Local Time: {city_info['location']['localtime']}") 
                timezone = (f"Timezone: {city_info['location']['tz_id']}")
                cel = (f"Temperature: {city_info['current']['temp_c']}°C")
                far = (f"Temperature: {city_info['current']['temp_f']}°F") 
                isday = (f"Is it day? {city_info['current']['is_day']}") 
                wcond = (f"Weather condition: {city_info['current']['condition']['text']}") 
                winfkph = (f"Wind speed: {city_info['current']['wind_kph']} kph")
                windmph = (f"Wind speed: {city_info['current']['wind_mph']} mph") 
                winddegree = (f"Wind degree: {city_info['current']['wind_degree']}")  
                winddir = (f"Wind direction: {city_info['current']['wind_dir']}") 
                precipmm = (f"Precipitation: {city_info['current']['precip_mm']} mm")
                precipin = (f"Precipitation: {city_info['current']['precip_in']} in")
                humidity = (f"Humidity: {city_info['current']['humidity']}%") 
                feelslikec = (f"Feels like: {city_info['current']['feelslike_c']}°C") 
                feelslikef = (f"Feels like: {city_info['current']['feelslike_f']}°F") 
                windchillc = (f"Wind chill: {city_info['current']['windchill_c']}°C") 
                windchillf = (f"Wind chill: {city_info['current']['windchill_f']}°F") 
                heatindexc = (f"Heat index: {city_info['current']['heatindex_c']}°C") 
                heatindexf = (f"Heat index: {city_info['current']['heatindex_f']}°F") 
                dewpointc = (f"Dew point: {city_info['current']['dewpoint_c']}°C") 
                dewpointf = (f"Dew point: {city_info['current']['dewpoint_f']}°F")
                uv = (f"UV index: {city_info['current']['uv']}")
                gust_mph = (f"Gust speed: {city_info['current']['gust_mph']} mph")
                gust_kph = (f"Gust speed: {city_info['current']['gust_kph']} kph")

            print("-------------------City Info--------------------")
            print(cit)
            print(cou)
            print(lat)
            print(lon)
            print(localtime)
            print(timezone)
            print(humidity) 
            print("-------------------------------------------------")
            choice1 = input ("Type 'details' to see further information")
            choice2 = input ("Type S to save city, Type F to favoutite city")


        elif choice == "2":
            print("Showing saved city's...")  # Replace with function later

        elif choice == "3":
            print("Showing favourited city's...")  # Replace with function later

        elif choice == "4":
            settings_menu()  # Now opens the submenu properly

        elif choice == "5":
            print("Exiting Weather App.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()