import os
from typing import TypedDict
import json
import requests
from dotenv import load_dotenv

from app_types.openweathermap import DailyAggregationResponse, WeatherApiResponse, GeocodingResponse


class openweathermap:
    load_dotenv()

    @staticmethod
    def daily_aggregation(lat,long,date) -> DailyAggregationResponse:
        """Daily aggregation of weather data for 45+ years archive and 1.5 years ahead forecast"""

        OPENWEATHERMAP_KEY = os.getenv('OPENWEATHERMAP_KEY')
        UNITS = os.getenv('UNITS','metric')

        r = requests.get(f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={long}&date={date}&units={UNITS}&appid={OPENWEATHERMAP_KEY}")

        if r.status_code != 200:
            raise Exception("OpenWeatherMap API Error")

        return r.json()

    @staticmethod
    def  current_weather_and_forecasts(lat,long) -> WeatherApiResponse:
        """Current weather and forecasts:
                minute forecast for 1 hour
                hourly forecast for 48 hours
                daily forecast for 8 days"""

        OPENWEATHERMAP_KEY = os.getenv('OPENWEATHERMAP_KEY')
        UNITS = os.getenv('UNITS','metric')

        r = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={long}&units={UNITS}&appid={OPENWEATHERMAP_KEY}")

        if r.status_code != 200:
            raise Exception("OpenWeatherMap API Error")

        return r.json()

    @staticmethod
    def geocode(city_name)-> GeocodingResponse:
        OPENWEATHERMAP_KEY = os.getenv('OPENWEATHERMAP_KEY')

        r = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q=lisbon&limit=1&appid={OPENWEATHERMAP_KEY}")

        if r.status_code != 200:
            raise Exception("OpenWeatherMap API Error")

        resp_json = r.json()
        parsed: GeocodingResponse = {"lat": resp_json[0]["lat"], "lon": resp_json[0]["lon"]}
        return parsed
