import requests 
  
api_key = "6b2b2b28d67b4bd892b233321262303" 

base_url = "http://api.weatherapi.com/v1" 
  
def get_city_info(name): 
    url = f"{base_url}/current.json?key={api_key}&q={city_name}&aqi=no" 
    response = requests.get(url) 
    print(response)
    
    if response.status_code == 200: 
        city_data = response.json() 
        return city_data
    else: 
        print(f"Failed to retrieve data {response.status_code}")
 
city_name = input ("Enter City: ") 
city_info = get_city_info(city_name) 
 
if city_info:
     print(city_info["location"]["name"])
     print(city_info["location"]["country"]) 
     print(city_info["location"]["localtime"])