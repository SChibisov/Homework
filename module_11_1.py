from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
# insert your real key here!
access_key = "8916bc19-aaec-4a54-ac64-a0938810c31f"

headers = {
    "X-Yandex-Weather-Key": access_key
}

query = """{
  weatherByPoint(request: { lat: 55.117082, lon: 36.597014 }) {
    forecast {
      days(limit: 2) {
        time
        sunriseTime
        sunsetTime
        parts {
          morning {
            avgTemperature
          }
          day {
            avgTemperature
          }
          evening {
            avgTemperature
          }
          night {
            avgTemperature
          }
        }
      }
    }
  }
}"""

response = requests.post('https://api.weather.yandex.ru/graphql/query', headers=headers, json={'query': query})
weather_data = response.json()
with open('weather_data_1.json', 'w') as file:
    json.dump(weather_data, file)
print(type(response))
print(type(weather_data))
pprint(weather_data)
