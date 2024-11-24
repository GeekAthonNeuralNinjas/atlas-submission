from typing import TypedDict, Optional, List


class WindMax(TypedDict):
    direction: float
    speed: float

class Wind(TypedDict):
    max: WindMax

class Temperature(TypedDict):
    afternoon: float
    evening: float
    max: float
    min: float
    morning: float
    night: float

class Precipitation(TypedDict):
    total: float

class Pressure(TypedDict):
    afternoon: float

class Humidity(TypedDict):
    afternoon: float

class CloudCover(TypedDict):
    afternoon: float

class DailyAggregationResponse(TypedDict):
    cloud_cover: CloudCover
    date: str
    humidity: Humidity
    lat: float
    lon: float
    precipitation: Precipitation
    pressure: Pressure
    temperature: Temperature
    tz: str
    units: str
    wind: Wind

# Reuse WindMax and Temperature where applicable
class Weather(TypedDict):
    id: int
    main: str
    description: str
    icon: str


class CurrentWeather(TypedDict):
    dt: int
    sunrise: int
    sunset: int
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    dew_point: float
    uvi: float
    clouds: int
    visibility: int
    wind_speed: float
    wind_deg: int
    wind_gust: Optional[float]
    weather: List[Weather]


class MinutelyWeather(TypedDict):
    dt: int
    precipitation: float


class HourlyWeather(TypedDict):
    dt: int
    temp: float
    feels_like: float
    pressure: int
    humidity: int
    dew_point: float
    uvi: float
    clouds: int
    visibility: int
    wind_speed: float
    wind_deg: int
    wind_gust: Optional[float]
    weather: List[Weather]
    pop: float


class DailyFeelsLike(TypedDict):
    day: float
    night: float
    eve: float
    morn: float


class DailyTemp(TypedDict):
    day: float
    min: float
    max: float
    night: float
    eve: float
    morn: float



class DailyWeather(TypedDict):
    dt: int
    sunrise: int
    sunset: int
    moonrise: int
    moonset: int
    moon_phase: float
    summary: str
    temp: DailyTemp
    feels_like: DailyFeelsLike
    pressure: int
    humidity: int
    dew_point: float
    wind_speed: float
    wind_deg: int
    wind_gust: Optional[float]
    weather: List[Weather]
    clouds: int
    pop: float
    rain: Optional[float]
    uvi: float


class Alert(TypedDict):
    sender_name: str
    event: str
    start: int
    end: int
    description: str
    tags: List[str]


class WeatherApiResponse(TypedDict):
    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    current: CurrentWeather
    minutely: Optional[List[MinutelyWeather]]
    hourly: List[HourlyWeather]
    daily: List[DailyWeather]
    alerts: Optional[List[Alert]]

class GeocodingResponse(TypedDict):
    lat: float
    lon: float

