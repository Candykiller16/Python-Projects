import json

import requests
from pydantic import BaseModel, validator, Extra


class Temperature(BaseModel):
    class Config:
        extra = Extra.forbid

    temp: float
    feels_like: float
    temp_min: float
    temp_max: float

    @validator('temp')
    def cels_in_far(cls, value):
        return round(value * 9 / 5 + 32, 2)

class Weather(BaseModel):
    temperature: Temperature
    pressure: int
    description: str
    name: str



class Coordinate:

    def _init__(self, latitude, longitude):
        self.__longitude = longitude
        self.__latitude = latitude

    def get_weather_information(self):
        req = requests.get(f'https://fcc-weather-api.glitch.me/api/'
                           f'current?lat={self.__latitude}&lon={self.__longitude}')
        try:
            if req.status_code != 200:
                raise Exception(f'Error request (status code:{req.status_code})')
            j_data = json.loads(req.text)
            try:
                _feels_like = j_data.get['main']['feels_like']
            except:
                _feels_like = 0
            data = {'temperature':{'temp': j_data['main']['temp'],
                                   'feels_like': j_data['main']['feels_like'],
                                   'temp_min': j_data['main']['temp_min'],
                                   'temp_max': j_data['main']['temp_max']
                                   },
                    'pressure': j_data['main']['pressure'],
                    'description': j_data['weather'][0]['description'],
                    'name': j_data['name']
                    }
        except:
            return None
        return Weather(**data)

Weather.parse_file('weather.json')
#
from unittest.mock import Mock, MagicMock

def test_get_weather_information(mocker):
    mocker.patch.object(
                        requests,
                        'get',
                        return_value=Mock(
                            status_code = 200,
                            text=json.dumps(
                                {
                                    'coord':{'lon': 139, 'lat': 35},
                                    'weather':[{'id': 801, 'main':"Clouds", 'description': "few clouds"}],
                                    'base': "stations",
                                    'main':{'temp':6.67, 'feels_like': 6.67, 'temp_min': 6.67, 'temp_max': 6.67,
                                            'pressure': 1032, 'humidity': 81, 'visibility': 10000},
                                    'wind':{'speed': 1.04, 'deg': 121, 'gust': 1.71},
                                    'clouds': {'all': 12},
                                    'dt': 1618134659,
                                    'sys': {'type': 3, 'id': 2019346, 'country': "JP", 'sunrise': 1618085848,
                                            'sunset': 1618132339},
                                    'timezone': 32400,
                                    'id': 1851632,
                                    'name':"Shuzenji",
                                    'cod': 200
                                    }
                                )
                            )
                        )


coordinate = Coordinate(51.89, 26.85)
# weather = coordinate.get_weather_information()
# print(f'In {weather.name} {weather.temperature.temp} F')
    result = coordinate.get_weather_information()

    expected = Weather(
        temperature = Temperature.construct(
            temp = 44.0,
            feels_like = 6.67,
            temp_min = 	6.67,
            temp_max = 6.67
        ),
        pressure = 1032,
        description = 'few clouds',
        name = 'Shuzenji'
    )

    assert result == expected

