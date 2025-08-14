import requests

def get_weather(city, units='metric', api_key='api_key'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)
    content = response.json()
    #open file
    with open("data.txt", 'a') as file:
        for item in content['list']:
            file.write(f"{item['dt_txt']}, {item['main']['temp']}, {item['weather'][0]['description']} \n")
        # return content

print(get_weather(city='London'))


