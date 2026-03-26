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