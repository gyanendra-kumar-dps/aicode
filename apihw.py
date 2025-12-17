import requests
def lat_lon(city):
    cities={
        "bangalore":{'latitude':12.9716,'longitude':77.5946,'current_weather':True},
        "chennai":{'latitude':13.0827,'longitude':80.2707,'current_weather':True},
        "delhi":{'latitude':28.6139,'longitude':80.2707,'current_weather':True},
        "mumbai":{'latitude':19.0760,'longitude':72.8777,'current_weather':True}
    }
    return cities[city]
inp=input("Enter city name:")
url="https://api.open-meteo.com/v1/forecast"
response=requests.get(url,params=lat_lon(inp.lower()))
if response.status_code==200:
    data=response.json()
    tempdata=data['current_weather']
    print(f'current weather in {inp}')
    print(f'temperature:- {tempdata['temperature']}')
    print(f'wind speed:- {tempdata['windspeed']}')
    print(f'date:- {tempdata['time']}')