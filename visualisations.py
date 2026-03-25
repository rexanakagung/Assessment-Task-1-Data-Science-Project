def plot_temperature(city_info):
    forecast_days = city_info['forecast']['forecast_days']
    days = [day['day']['maxtemp_c']for day in forecast_days]
    min_temps = [day['day']['mintemp_c'] for day in forecast_days]