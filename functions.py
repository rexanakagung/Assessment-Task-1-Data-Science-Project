import requests 
  
api_key = "6b2b2b28d67b4bd892b233321262303" 

base_url = "http://api.weatherapi.com/v1" 
  
def get_city_info(name): 
    url = f"{base_url}/current.json?key={api_key}&q={city_name}&aqi=no" 
    response = requests.get(url) 
    print(response)
 
city_name = "London" 
get_city_info(city_name)