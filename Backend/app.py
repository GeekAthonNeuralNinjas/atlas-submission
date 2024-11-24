from flask import Flask, request

from externalAPI.bedrock.example_request import AtlasBedrock
from externalAPI.googlePlaces import GooglePlacesAPI
from externalAPI.openweathermap import openweathermap

app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Test 23"

@app.route('/demoPlan')
def demoPlan():
    return ""

@app.route('/plan',methods=['GET'])
def plan():
    print("planing")
    city = request.args.get('city')
    start_date = request.args.get('start_data')
    duration = request.args.get('duration')
    flavor = request.args.get('flavor')

    return AtlasBedrock.plan_trip(city,start_date,duration,flavor)

@app.route('/change',methods=['post'])
def change():
    print("generating changes")
    city = request.args.get('city')
    start_date = request.args.get('start_data')
    duration = request.args.get('duration')
    old_prompt = request.form.get('old')
    prompt = request.form.get('prompt')
    return AtlasBedrock.change_trip(city,start_date,duration,old_prompt,arbitrary=prompt)

@app.route('/weather/daily_aggregation', methods=['GET'])
def weather_daily_aggregation():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    start_date = request.args.get('startDate')

    return openweathermap.daily_aggregation(lat, lon, start_date)


@app.route('/place', methods=['GET'])
def place():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    radius = float(request.args.get('radius', 500.0))
    included_types = request.args.getlist('includedTypes')
    max_result_count = int(request.args.get('maxResultCount', 20))

    # Call the GooglePlacesAPI static method
    result = GooglePlacesAPI.search_nearby_places(lat, lon, radius, included_types, max_result_count)
    return result

# @app.route('/search_location', methods=['GET'])
# # def search_location():
# #     search_query = request.args.get('searchQuery')
# #     latitude = request.args.get('latitude')
# #     longitude = request.args.get('longitude')
# #     category = request.args.get('category')
# #     phone = request.args.get('phone')
# #     radius = request.args.get('radius')
# #     radius_unit = request.args.get('radiusUnit', 'km')
# #     language = request.args.get('language', 'en')
# #
# #     if not search_query:
# #         return jsonify({"error": "searchQuery is required"}), 400
# #     if not latitude or not longitude:
# #         return jsonify({"error": "Both latitude and longitude are required"}), 400
# #
# #     try:
# #         result = TripAdvisorAPI.get_first_location_details(
# #             search_query, latitude=latitude, longitude=longitude
# #         )
# #         return result
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
