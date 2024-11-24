from externalAPI.googlePlaces import GooglePlacesAPI

world_cities = [
    "lisbon"
    # European Cities (50 from the previous list)
    # "Lisbon", "Madrid", "Barcelona", "Paris", "Lyon", "Berlin", "Munich",
    # "Hamburg", "Rome", "Milan", "Venice", "Florence", "Vienna", "Budapest",
    # "Prague", "Warsaw", "Kraków", "Athens", "Thessaloniki", "Dublin", "Belfast",
    # "Amsterdam", "Rotterdam", "Brussels", "Antwerp", "Copenhagen", "Oslo",
    # "Stockholm", "Helsinki", "Reykjavik", "Zurich", "Geneva", "Luxembourg City",
    # "Tallinn", "Riga", "Vilnius", "Bratislava", "Ljubljana", "Sarajevo",
    # "Belgrade", "Sofia", "Bucharest", "Tirana", "Podgorica", "Skopje",
    # "Valletta", "Monaco", "San Marino", "Andorra la Vella", "Vaduz",
    #
    # # North American Cities
    # "New York City", "Los Angeles", "Chicago", "Houston", "Toronto", "Vancouver",
    # "Mexico City", "Monterrey", "Guadalajara", "San Francisco", "Miami",
    # "Washington, D.C.", "Dallas", "Atlanta", "Boston", "Philadelphia", "Seattle",
    # "Montreal", "Calgary", "Ottawa",
    #
    # # South American Cities
    # "São Paulo", "Rio de Janeiro", "Buenos Aires", "Lima", "Bogotá", "Santiago",
    # "Quito", "Caracas", "Montevideo", "Asunción", "La Paz", "Brasília",
    # "Medellín", "Guayaquil", "Córdoba", "Rosario", "Fortaleza", "Salvador",
    #
    # # Asian Cities
    # "Tokyo", "Seoul", "Beijing", "Shanghai", "Mumbai", "Delhi", "Bangkok",
    # "Jakarta", "Manila", "Singapore", "Kuala Lumpur", "Hong Kong",
    # "Taipei", "Chennai", "Osaka", "Karachi", "Dhaka", "Istanbul", "Riyadh",
    # "Dubai", "Abu Dhabi", "Doha", "Tehran", "Baghdad", "Hanoi", "Ho Chi Minh City",
    # "Phnom Penh", "Ulaanbaatar", "Colombo", "Amman", "Kuwait City",
    #
    # # African Cities
    # "Cairo", "Johannesburg", "Cape Town", "Lagos", "Nairobi", "Algiers",
    # "Casablanca", "Tunis", "Accra", "Addis Ababa", "Dar es Salaam",
    # "Kigali", "Kampala", "Luanda", "Harare", "Dakar", "Abidjan",
    # "Windhoek", "Kinshasa", "Tripoli",
    #
    # # Oceania Cities
    # "Sydney", "Melbourne", "Brisbane", "Perth", "Auckland", "Wellington",
    # "Canberra", "Adelaide", "Hobart", "Christchurch", "Suva",
    #
    # # Middle Eastern Cities
    # "Jerusalem", "Tel Aviv", "Beirut", "Muscat", "Mecca", "Medina", "Sana'a",
    # "Mashhad", "Aleppo", "Damascus", "Basra",
    #
    # # Additional Major Global Cities
    # "London", "Edinburgh", "Glasgow", "Birmingham", "Manchester",
    # "Mumbai", "Chennai", "Hyderabad", "Ahmedabad", "Jaipur",
    # "St. Petersburg", "Moscow", "Vladivostok", "Novosibirsk",
    # "Kazan", "Yekaterinburg", "Seoul", "Busan", "Incheon",
    # "Jakarta", "Bandung", "Surabaya", "Bangkok", "Chiang Mai",
    # "Ho Chi Minh City", "Hanoi", "Vientiane", "Yangon", "Mandalay"
]

for city in world_cities:
    GooglePlacesAPI.fetch_data_from_city(city)
