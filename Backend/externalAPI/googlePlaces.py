import os

import requests
from dotenv import load_dotenv

from externalAPI.openweathermap import openweathermap


class GooglePlacesAPI:
    load_dotenv()

    @staticmethod
    def search_nearby_places(lat, lon, radius=5000.0, included_types=None, max_result_count=20):
        # Load API key from environment variables
        PLACES_API_KEY = os.getenv('PLACES_API_KEY')

        if not included_types:
            included_types = ['restaurant']
            # included_types = ['restaurant']
            #                   'bus_station','cafe','church','library','mosque','museum','night_club','park','stadium','tourist_attraction','zoo']
        payload = {
            'includedTypes': included_types,
            'maxResultCount': max_result_count,
            'locationRestriction': {
                'circle': {
                    'center': {
                        'latitude': lat,
                        'longitude': lon
                    },
                    'radius': radius
                }
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': PLACES_API_KEY,
            'X-Goog-FieldMask': '*'
        }

        # Make the API request
        response = requests.post(
            "https://places.googleapis.com/v1/places:searchNearby?fields=places.displayName,places.location,places.primaryType,places.rating,places.currentOpeningHours.weekdayDescriptions,places.formattedAddress,places.internationalPhoneNumber,places.websiteUri",
            json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(response.json())

        return response.json()

    @staticmethod
    def fetch_data_from_city(city):
        # Add extra context
        coordinates = openweathermap.geocode(city)

        restaurants = GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'])['places']
        # print(restaurants)
        # 'bus_station','cafe','church','library','mosque','museum','night_club','park','stadium','tourist_attraction','zoo']

        museums = \
            GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'], included_types=['museum'])[
                'places']
        tourist_attractions = GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'],
                                                                   included_types=['tourist_attraction'])['places']
        zoos = GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'], included_types=['zoo'])[
            'places']
        # hotels = GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'],included_types=['hotels'])['places']
        cafes = GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'], included_types=['cafe'])[
            'places']
        night_clubs = \
            GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'], included_types=['night_club'])[
                'places']
        bus_stations = \
            GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'],
                                                 included_types=['bus_station'])[
                'places']
        church = \
            GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'], included_types=['church'])[
                'places']
        stadiums = \
            GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'], included_types=['stadium'])[
                'places']
        mosque = \
            GooglePlacesAPI.search_nearby_places(coordinates['lat'], coordinates['lon'], included_types=['mosque'])[
                'places']

        pois = museums + tourist_attractions + zoos + restaurants + cafes + night_clubs + bus_stations + church + stadiums + mosque
        return pois

    @staticmethod
    def find_hotels(city):
        PLACES_API_KEY = os.getenv('PLACES_API_KEY')
        payload = {
            "textQuery": f"Hotels in {city}",
            "maxResultCount": 2,
        }

        headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': PLACES_API_KEY,
            'X-Goog-FieldMask': '*'
        }

        # Make the API request
        response = requests.post(
            "https://places.googleapis.com/v1/places:searchText?fields=places.displayName,places.location,places.primaryType,places.rating,places.currentOpeningHours.weekdayDescriptions,places.formattedAddress,places.internationalPhoneNumber,places.websiteUri",
            json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(response.json())

        return response.json()
