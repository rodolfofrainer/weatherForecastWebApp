import os
import env
import requests


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={os.getenv('API_KEY')}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == '__main__':
    print(get_data('dublin'))
