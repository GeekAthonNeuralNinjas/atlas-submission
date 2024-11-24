import time
from datetime import datetime, timedelta
from multiprocessing.resource_tracker import register
from os import system
from pickle import FALSE

import json

from externalAPI.googlePlaces import GooglePlacesAPI
from externalAPI.openweathermap import openweathermap

import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content


def is_within_8_days_in_future(input_date):
    today = datetime.now().date()
    future_limit = today + timedelta(days=8)
    return today <= input_date <= future_limit


class AtlasBedrock:
    @staticmethod
    def plan_trip(city, start_date, duration, flavor='fun'):
        """
        Install an additional SDK for JSON schema support Google AI Python SDK

        $ pip install google.ai.generativelanguage
        """

        genai.configure(api_key="AIzaSyBvBYCnmPNmhToJ-iQZELxF1ViuClIj1BE")

        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_schema": content.Schema(
                type=content.Type.OBJECT,
                enum=[],
                required=["name", "places","isLandmark"],
                properties={
                    "name": content.Schema(
                        type=content.Type.STRING,
                    ),
                    "places": content.Schema(
                        type=content.Type.ARRAY,
                        items=content.Schema(
                            type=content.Type.OBJECT,
                            enum=[],
                            required=["name", "coordinates", "city", "arrival_hour", "arrival", "type"],
                            properties={
                                "name": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "rating": content.Schema(
                                    type=content.Type.NUMBER,
                                ),
                                "description": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "coordinates": content.Schema(
                                    type=content.Type.OBJECT,
                                    properties={
                                        "lat": content.Schema(
                                            type=content.Type.NUMBER,
                                        ),
                                        "log": content.Schema(
                                            type=content.Type.NUMBER,
                                        ),
                                    },
                                ),
                                "isLandmark": content.Schema(
                                    type=content.Type.BOOLEAN,
                                ),
                                "city": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "reason": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "arrival_hour": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "arrival": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "duration": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "type": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "adress": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "phone": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "website": content.Schema(
                                    type=content.Type.STRING,
                                ),
                            },
                        ),
                    ),
                    "description": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

        coordinates = openweathermap.geocode(city)
        if is_within_8_days_in_future:
            weatherParts = [
                "Use the following weather information to pick the best to visit outdoor and indoor places",
                json.dumps(
                    openweathermap.current_weather_and_forecasts(lat=coordinates["lat"], long=coordinates["lon"]))
            ]
            print("fetched weather")
        else:
            weatherParts = ["Take into consideration the season and weather pattern in that country in that time"]
        hotels = GooglePlacesAPI.find_hotels(city)
        print(f"Fetched {len(hotels['places'])} hotels")

        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "You are a travel agent creating itineraries. Provide a detailed plan for the requested destination, including top restaurants, landmarks, cultural sites, and beaches (if relevant). Focus only on highly relevant places, avoiding repetition or irrelevant stops. Ensure the trip fits the desired duration, includes time for meals and rest, and minimizes travel distances. Use bullet points for concise reasons behind each choice. Provide a trip description focused solely on the destinations. Coordinates must be copied exactly. Accuracy is critical mistakes or deviations will lead to lives being lost",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        f"Use the following points to make the best decisions possibles. Always ensure that the isLandmark flag is set with a true of false value. Make sure that the place description is about the place.",
                        json.dumps(GooglePlacesAPI.fetch_data_from_city(city))
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        f"If it's more than a one day trip make sure you also take into consideration a place to sleep, use the following list as reference to pick said place. Note that it is preferred to stay in one place",
                        json.dumps(hotels)
                    ],
                },
                {
                    "role": "user",
                    "parts": weatherParts
                }
            ]
        )
        query = f"plan a trip to {city} that lasts for {duration} days and starts on {start_date} that is {flavor}"
        response = chat_session.send_message(query)
        resp_json = {}
        try:
            resp_json = json.loads(response.text)
        except:
            with open('error.json', 'w', encoding='utf-8') as f:
                f.write(response.text)

        return resp_json

    @staticmethod
    def change_trip(city, start_date, duration, flavor='fun', original_prompt={}, arbitrary =""):
        genai.configure(api_key="AIzaSyBvBYCnmPNmhToJ-iQZELxF1ViuClIj1BE")
        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_schema": content.Schema(
                type=content.Type.OBJECT,
                enum=[],
                required=["name", "places"],
                properties={
                    "name": content.Schema(
                        type=content.Type.STRING,
                    ),
                    "places": content.Schema(
                        type=content.Type.ARRAY,
                        items=content.Schema(
                            type=content.Type.OBJECT,
                            enum=[],
                            required=["name", "coordinates", "city", "arrival_hour", "arrival", "type"],
                            properties={
                                "name": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "rating": content.Schema(
                                    type=content.Type.NUMBER,
                                ),
                                "description": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "coordinates": content.Schema(
                                    type=content.Type.OBJECT,
                                    properties={
                                        "lat": content.Schema(
                                            type=content.Type.NUMBER,
                                        ),
                                        "log": content.Schema(
                                            type=content.Type.NUMBER,
                                        ),
                                    },
                                ),
                                "isLandmark": content.Schema(
                                    type=content.Type.BOOLEAN,
                                ),
                                "city": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "reason": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "arrival_hour": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "arrival": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "duration": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "type": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "adress": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "phone": content.Schema(
                                    type=content.Type.STRING,
                                ),
                                "website": content.Schema(
                                    type=content.Type.STRING,
                                ),
                            },
                        ),
                    ),
                    "description": content.Schema(
                        type=content.Type.STRING,
                    ),
                },
            ),
            "response_mime_type": "application/json",
        }

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

        coordinates = openweathermap.geocode(city)
        if is_within_8_days_in_future:
            weatherParts = [
                "Use the following weather information to pick the best to visit outdoor and indoor places",
                json.dumps(
                    openweathermap.current_weather_and_forecasts(lat=coordinates["lat"], long=coordinates["lon"]))
            ]
            print("fetched weather")
        else:
            weatherParts = ["Take into consideration the season and weather pattern in that country in that time"]
        hotels = GooglePlacesAPI.find_hotels(city)
        print(f"Fetched {len(hotels['places'])} hotels")

        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "You are a travel agent creating itineraries. Provide a detailed plan for the requested destination, including top restaurants, landmarks, cultural sites, and beaches (if relevant). Focus only on highly relevant places, avoiding repetition or irrelevant stops. Ensure the trip fits the desired duration, includes time for meals and rest, and minimizes travel distances. Use bullet points for concise reasons behind each choice. Provide a trip description focused solely on the destinations. Coordinates must be copied exactly. Accuracy is critical mistakes or deviations will lead to lives being lost",
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        f"Use the following points to make the best decisions possibles. Always ensure that the isLandmark flag is set with a true of false value. Make sure that the place description is about the place.",
                        json.dumps(GooglePlacesAPI.fetch_data_from_city(city))
                    ],
                },
                {
                    "role": "user",
                    "parts": [
                        f"If it's more than a one day trip make sure you also take into consideration a place to slee, use the following list as reference to pick said place. Note that it is preferred to stay in one place",
                        json.dumps(hotels)
                    ],
                },
                {
                    "role": "user",
                    "parts": weatherParts
                },
                {
                    "role": "user",
                    "parts": ["Based on this previously generated plan",
                              json.dumps(original_prompt)
                              ]
                },

            ]
        )
        query = f"change the provided trip to lasts for {duration} days and start on {start_date} that is {flavor}"
        if arbitrary != "":
            text = f" and {arbitrary}"
            query = query+text
        response = chat_session.send_message(query)
        resp_json = {}
        try:
            resp_json = json.loads(response.text)
        except:
            with open('error.json', 'w', encoding='utf-8') as f:
                f.write(response.text)

        return resp_json
