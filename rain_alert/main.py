import requests
import os
from twilio.rest import Client


# api_key = '75d763a0a38e8dc175b175a8f2bbcaea'
api_key = os.environ.get('OWM_API_KEY')
account_sid = 'AC05a92e883b861d561df26a7f7c72369e'
auth_token = os.environ.get('AUTH_TOKEN')
# auth_token = 'da7645f99e38569cf2745562c66931db'

parameters = {
    'lat': -22.916208,
    'lon': -43.215544,
    'exclude': 'current,minutely,daily',
    'appid': api_key,
}

response = requests.get('https://api.openweathermap.org/data/3.0/onecall', params=parameters)
response.raise_for_status()

print(response)

weather_data = response.json()
first_twelve_hours = weather_data['hourly'][:12]

will_rain = False

# for num in range(12):
#     if first_twelve_hours[num]['weather'][0]['id'] < 700:
#         will_rain = True
for hourly_data in first_twelve_hours:
    weather_condition = hourly_data['weather'][0]['id']
    if weather_condition < 900:
        print(weather_condition)
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔.",
        from_='+15419098143',
        to='+233543166742'
    )

    print(message)

