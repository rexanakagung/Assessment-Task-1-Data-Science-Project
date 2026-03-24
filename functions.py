import requests 
  
api_key = "6b2b2b28d67b4bd892b233321262303" 

base_url = "http://api.weatherapi.com/v1" 
  
def get_city_info(name):
    url = f"{base_url}/current.json?key={api_key}&q={name}&aqi=no"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code} {response.text}")
        return None

# no direct input in module-level code; call get_city_info() from main.py as needed
