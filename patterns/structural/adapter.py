from abc import ABC, abstractmethod


class CoordinateProvider(ABC):
    @abstractmethod
    def get(self, city: str) -> tuple[float, float]: ...


class GeolocationAPI:
    @staticmethod
    def fetch_location(city: str) -> str:
        match city:
            case "Moscow":
                return "37.618423, 55.751244"
            case _:
                raise ValueError(f"Unknown city: {city}")


class GeoAdapter(CoordinateProvider):
    """
    Adapter (Wrapper, Translator) is a structural design pattern that allows objects with incompatible interfaces to work together.
    """

    def __init__(self, api: GeolocationAPI):
        self.api = api

    def get(self, city: str) -> tuple[float, float]:
        # Get string "longitude, latitude"
        data = self.api.fetch_location(city)
        # Разделяем строку и конвертируем в tuple (latitude, longitude)
        lon, lat = map(float, data.split(", "))
        return lat, lon  # Приводим к формату (lat, lon)
