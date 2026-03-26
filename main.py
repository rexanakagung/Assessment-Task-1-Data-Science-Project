import json

print("Welcome to the Weather App!")
input("Enter any letter to start: ") 

SAVED_CITIES_FILE = "saved_cities.json"
 
weather_icons = {
    "Sunny": "☀️",
    "Clear": "☀️",
    "Partly cloudy": "⛅",
    "Cloudy": "☁️",
    "Overcast": "☁️",
    "Mist": "🌫️",
    "Patchy rain possible": "🌦️",
    "Patchy snow possible": "🌨️",
    "Patchy sleet possible": "🌨️",
    "Patchy freezing drizzle possible": "🌧️",
    "Thundery outbreaks possible": "⛈️",
    "Blowing snow": "🌨️",
    "Blizzard": "🌨️",
    "Fog": "🌫️",
    "Freezing fog": "🌫️",
    "Patchy light drizzle": "🌦️",
    "Light drizzle": "🌦️",
    "Freezing drizzle": "🌧️",
    "Heavy freezing drizzle": "🌧️",
    "Patchy light rain": "🌦️",
    "Light rain": "🌦️",
    "Moderate rain": "🌦️",
    "Heavy rain": "🌧️",
    "thunderstorm": "⛈️",
    # Add more conditions as needed
}


def load_saved_cities():
    try:
        with open(SAVED_CITIES_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    return []


def save_saved_cities(cities):
    with open(SAVED_CITIES_FILE, "w", encoding="utf-8") as file:
        json.dump(cities, file, indent=2)


def add_saved_city(city_name):
    cleaned_name = city_name.strip()
    if not cleaned_name:
        return False

    saved_cities = load_saved_cities()
    existing = {city.lower() for city in saved_cities}
    if cleaned_name.lower() in existing:
        return False

    saved_cities.append(cleaned_name)
    save_saved_cities(saved_cities)
    return True


def show_saved_cities_menu():
    saved_cities = load_saved_cities()
    print("\nSaved Cities")
    print("-" * 30)
    if not saved_cities:
        print("No saved cities yet.")
        return None

    for index, city in enumerate(saved_cities, start=1):
        print(f"{index}. {city}")

    while True:
        choice = input("Type a number to load a saved city, or 'r' to return: ").strip().lower()
        if choice == 'r':
            return None
        if choice.isdigit():
            city_index = int(choice)
            if 1 <= city_index <= len(saved_cities):
                return saved_cities[city_index - 1]
        print("Invalid input. Try again.")

def settings_menu():
    while True:
        print("\nSettings Menu")
        print("1. Erase Saved Cities")
        print("2. Back To Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            save_saved_cities([])
            print("Saved cities erased.")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")


from functions import get_city_info
from visualisations import plot_temperature, plot_uv_index, plot_wind_speed

def main():
    while True:
        print("\nWeather App Menu:")
        print("1. Search city")
        print("2. Saved Cities")
        print("3. Settings")
        print("4. Exit")
        choice = input("Choose an option: ")
        preselected_city = None

        if choice == "2":
            preselected_city = show_saved_cities_menu()
            if not preselected_city:
                continue
            choice = "1"

        if choice == "1":
            while True:
                print("")
                if preselected_city:
                    name = preselected_city
                else:
                    name = input("Enter city: ")
                print(f"Searching for {name}'s details...")
                city_info = get_city_info(name)
                if city_info:
                    break
                print(f"City '{name}' not found. Please try again.")
                if preselected_city:
                    break

            if not city_info:
                continue

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

            print("-" * 70)
            print("     📅 7-DAY FORECAST")
            print("-" * 70)
            print(f"     🌍 {city_info['location']['name']}, {city_info['location']['country']}") 
            print(f"     ⌛️ {city_info['location']['localtime']}")
            print("=" * 70)
            
            # Display forecast days with proper alignment
            import datetime
            if 'forecast' in city_info and 'forecastday' in city_info['forecast']:
                
                for i, day in enumerate(city_info['forecast']['forecastday'][:7]):
                    # Parse the date and get day name
                    date_obj = datetime.datetime.strptime(day['date'], '%Y-%m-%d')
                    
                    # Check if this is today
                    today = datetime.datetime.now().date()
                    forecast_date = date_obj.date()
                    
                    if forecast_date == today:
                        day_name = "Today"
                    else:
                        day_name = date_obj.strftime('%A')  # Full day name like "Monday"
                    
                    high_temp = int(day['day']['maxtemp_c'])
                    low_temp = int(day['day']['mintemp_c'])
                    condition = day['day']['condition']['text']
                    icon = weather_icons.get(condition, '🌤️')
                    rain_chance = day['day'].get('daily_chance_of_rain', 0)
                    
                    # Format with proper alignment
                    print(f"       {day_name:<12} {icon:<2} {high_temp}°/{low_temp}°  • {condition:<20} ({rain_chance}% rain)") 
            else:
                print("       Today")
                print("       Today")
            
           
            print("-" * 70)
            print("       🌡️  CURRENT CONDITIONS")
            print("-" * 70)
            print(f"       Wind Speed:      {city_info['current']['wind_kph']} km/h {city_info['current']['wind_dir']}")
            print(f"       Humidity:        {city_info['current']['humidity']}%")
            print(f"       Visibility:      {city_info['current']['vis_km']} km")
            print(f"       Precipitation:   {city_info['current']['precip_mm']} mm")
            print(f"       UV Index:        {city_info['current']['uv']}")
            print(f"       Pressure:        {city_info['current']['pressure_mb']} mb")
            print(f"       Dew Point:       {city_info['current']['dewpoint_c']}°C")
            print(f"       Wind Gust:       {city_info['current']['gust_kph']} kph")
            print("=" * 70)
            print("")

            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            choice1 = ""
            return_to_main_menu = False
            while True:
                choice1 = input("Type a day (Monday-Sunday) to see details, 's' to save, or 'r' to return: ").strip()

                if choice1.lower() == 'r':
                    return_to_main_menu = True
                    break

                if choice1.lower() == 's':
                    city_name = city_info['location']['name']
                    if add_saved_city(city_name):
                        print(f"{city_name} saved successfully.")
                    else:
                        print(f"{city_name} is already in saved cities.")
                    continue

                day_name = choice1.title()
                if day_name in days_of_week:
                    choice1 = day_name
                    break

                print("Invalid input. Try again.")

            if return_to_main_menu:
                continue

            if choice1 in days_of_week:
                # find forecast entry for selected day
                selected = None
                for day in city_info['forecast']['forecastday']:
                    import datetime
                    date_obj = datetime.datetime.strptime(day['date'], '%Y-%m-%d')
                    if date_obj.strftime('%A') == choice1:
                        selected = day['day']
                        break

                if selected:
                    print("")
                    print("-" * 70)
                    print(f"        🗓️ Forecast for {choice1}:")
                    print("-" * 70)
                    print(f"        Max Temp:           {selected['maxtemp_c']}°C")
                    print(f"        Min Temp:           {selected['mintemp_c']}°C")
                    feels_like = selected.get('avgtemp_c')
                    print(f"        Feels Like:         {feels_like}°C" if feels_like is not None else "        Feels Like: N/A")
                    print(f"        Condition:          {selected['condition']['text']}")
                    print(f"        Rain chance:        {selected.get('daily_chance_of_rain', 0)}%")
                    print(f"        Humidity:           {selected.get('avghumidity', 'N/A')}%")
                    print(f"        Visibility:         {selected.get('avgvis_km', 'N/A')} km")
                    print(f"        Pressure:           {selected.get('pressure_mb', 'N/A')} mb")
                    print(f"        Gust Speed:         {selected.get('maxwind_kph', 'N/A')} kph")
                    print(f"        UV Index:           {selected.get('uv', 'N/A')}")
                    print(f"        Precipitation:      {selected.get('totalprecip_mm', 'N/A')} mm")
                    print(f"        Wind Speed:         {selected.get('maxwind_kph', 'N/A')} kph")
                    print(f"        Wind Direction:     {selected.get('maxwind_dir', 'N/A')}")
                    print(f"        Sunrise:            {day['astro']['sunrise']}")
                    print(f"        Sunset:             {day['astro']['sunset']}")
                    print(f"        Moon Phase:         {day['astro']['moon_phase']}")
                    print(f"        Moon Illumination:  {day['astro']['moon_illumination']}%")
                    print(f"        Chance of Snow:     {selected.get('daily_chance_of_snow', 0)}%")
                    print(f"        Chance of Sleet:    {selected.get('daily_chance_of_sleet', 0)}%")
                    print("=" * 70)
                    print("")

            while True:
                choice2 = input("Type 'g' to see graphs or press Enter to continue: ").strip().lower()
                if choice2 in ('', 'g'):
                    break
                print("Invalid input. Try again.")

            if choice2 == 'g':
                while True:
                    print("")
                    print("-" * 70)
                    print("    📈 GRAPHS MENU")
                    print("-" * 70)
                    print("1.   🌡️ Hourly/Daily Temperature")
                    print("2.   🌞 Hourly/Daily UV Index")
                    print("3.   💨 Wind Speed Chart")
                    print("4.   🔙 Back to Main Menu")
                    print("=" * 70)

                    choice3 = input("Choose a graph to display (1-3) or '4' to go back: ")
                    if choice3 == "1":
                        plot_temperature(city_info)
                    elif choice3 == "2":
                        plot_uv_index(city_info)
                    elif choice3 == "3":
                        plot_wind_speed(city_info)
                    elif choice3 == "4":
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "3":
            settings_menu()  # Now opens the submenu properly

        elif choice == "4":
            print("Exiting Weather App.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()