def plot_temperature(city_info):
    forecast_days = city_info['forecast']['forecast_days']
    days = [day['day']['maxtemp_c']for day in forecast_days]
    min_temps = [day['day']['mintemp_c'] for day in forecast_days] 
     
    plt.figure(figsize=(10, 5)) 
    plt.plot(days, max_temps, marker='o', label='Max Temp (C)', color='tomato')
    plt.plot(days, max_temps, marker='o', label='Min Temp (C)', color='steelblue')
    plt.fill_between(days, min_temps, aplha=0.1, color='orange')
    plt.title(f"7-Day Temperature Forecast - {city_info('location')('name')}")
    plt.xlabel('Date')
    plt.ylabel('Temparature (C)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show() 
     
def plot_uv_index(city_info):
    forecast_days = city_info['forecast']['forecast_days']
    days = [day['date'] for day in forecast_days]
    uv_indices = [day['day']['uv'] for day in forecast_days]
    
    plt.figure(figsize=(10, 5))
    plt.plot(days, uv_indices, marker='o', label='UV Index', color='purple')
    plt.title(f"7-Day UV Index Forecast - {city_info['location']['name']}")
    plt.xlabel('Date')
    plt.ylabel('UV Index')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_wind_speed(city_info):
    forecast_days = city_info['forecast']['forecast_days']
    days = [day['date'] for day in forecast_days]
    wind_speeds = [day['day']['maxwind_kph'] for day in forecast_days]
    
    plt.figure(figsize=(10, 5))
    plt.plot(days, wind_speeds, marker='o', label='Max Wind Speed (kph)', color='green')
    plt.title(f"7-Day Wind Speed Forecast - {city_info['location']['name']}")
    plt.xlabel('Date')
    plt.ylabel('Wind Speed (kph)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()