import requests

def get_weather(city):
    api_key = 'api-key-here'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        print(f'Weather in {city}: {weather}, {temp}°C')
    else:
        print(f'City {city} not found. Error: {data["message"]}')

# Example usage
get_weather('Pangasinan')

