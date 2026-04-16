import time
import logging
from typing import Optional

import googlemaps
from src.models import Business, Review

logger = logging.getLogger(__name__)

DETAILS_FIELDS = [
    "name",
    "formatted_address",
    "formatted_phone_number",
    "international_phone_number",
    "website",
    "url",
    "rating",
    "user_ratings_total",
    "price_level",
    "type",
    "business_status",
    "geometry",
    "photo",
    "icon",
    "editorial_summary",
    "current_opening_hours",
    "address_component",
    "wheelchair_accessible_entrance",
    "serves_beer",
    "serves_wine",
    "serves_vegetarian_food",
    "takeout",
    "delivery",
    "dine_in",
    "curbside_pickup",
    "reservable",
    "serves_breakfast",
    "serves_lunch",
    "serves_dinner",
    "serves_brunch",
    "review",
]


class PlacesClient:
    def __init__(self, api_key: str):
        self.gmaps = googlemaps.Client(key=api_key)
        self._requests_count = 0

    @property
    def requests_count(self):
        return self._requests_count

    def nearby_search(
        self,
        lat: float,
        lng: float,
        radius: int = 500,
        place_type: Optional[str] = None,
        keyword: Optional[str] = None,
        page_token: Optional[str] = None,
    ) -> tuple[list[dict], Optional[str]]:
        try:
            self._requests_count += 1
            results = self.gmaps.places_nearby(
                location=(lat, lng),
                radius=radius,
                type=place_type,
                keyword=keyword,
                page_token=page_token,
            )
            places = results.get("results", [])
            next_token = results.get("next_page_token")
            time.sleep(2)
            return places, next_token
        except googlemaps.exceptions.ApiError as e:
            logger.error(f"Nearby search API error: {e}")
            return [], None
        except Exception as e:
            logger.error(f"Nearby search error: {e}")
            return [], None

    def get_place_details(self, place_id: str) -> Optional[dict]:
        try:
            self._requests_count += 1
            result = self.gmaps.place(
                place_id=place_id,
                fields=DETAILS_FIELDS,
            )
            time.sleep(0.1)
            return result.get("result", {})
        except googlemaps.exceptions.ApiError as e:
            logger.error(f"Place details API error for {place_id}: {e}")
            return None
        except Exception as e:
            logger.error(f"Place details error for {place_id}: {e}")
            return None

    def text_search(
        self, query: str, location: tuple = None, radius: int = 50000
    ) -> list[dict]:
        try:
            self._requests_count += 1
            kwargs = {"query": query}
            if location:
                kwargs["location"] = location
                kwargs["radius"] = radius
            results = self.gmaps.places(**kwargs)
            time.sleep(2)
            return results.get("results", [])
        except Exception as e:
            logger.error(f"Text search error: {e}")
            return []

    @staticmethod
    def parse_review(review_data: dict) -> Review:
        return Review(
            author_name=review_data.get("author_name", ""),
            author_url=review_data.get("author_url", ""),
            language=review_data.get("language", ""),
            profile_photo_url=review_data.get("profile_photo_url", ""),
            rating=review_data.get("rating", 0),
            relative_time_description=review_data.get("relative_time_description", ""),
            text=review_data.get("text", ""),
            time=review_data.get("time", 0),
        )

    @staticmethod
    def parse_address_components(components: list[dict]) -> dict:
        parsed = {
            "street_number": "",
            "street_name": "",
            "neighborhood": "",
            "city": "",
            "state": "",
            "postal_code": "",
            "country": "",
        }
        for comp in components:
            types = comp.get("types", [])
            long_name = comp.get("long_name", "")
            short_name = comp.get("short_name", "")

            if "street_number" in types:
                parsed["street_number"] = long_name
            elif "route" in types:
                parsed["street_name"] = long_name
            elif "sublocality_level_1" in types or "sublocality" in types:
                parsed["neighborhood"] = long_name
            elif "locality" in types:
                parsed["city"] = long_name
            elif "administrative_area_level_1" in types:
                parsed["state"] = short_name
            elif "postal_code" in types:
                parsed["postal_code"] = long_name
            elif "country" in types:
                parsed["country"] = long_name

        return parsed

    def parse_place(self, place_data: dict, include_reviews: bool = True) -> Business:
        addr_components = place_data.get("address_components", [])
        addr = self.parse_address_components(addr_components)

        geometry = place_data.get("geometry", {})
        location = geometry.get("location", {})

        types = place_data.get("types", [])
        primary_type = types[0] if types else ""

        reviews = []
        if include_reviews:
            for r in place_data.get("reviews", []):
                reviews.append(self.parse_review(r))

        photos = []
        for p in place_data.get("photos", []):
            photos.append(p.get("photo_reference", ""))

        opening_hours = {}
        hours_data = place_data.get("current_opening_hours", {})
        if hours_data:
            opening_hours = {
                "weekday_text": hours_data.get("weekday_text", []),
                "open_now": hours_data.get("open_now"),
            }

        website = place_data.get("website", "") or ""

        return Business(
            place_id=place_data.get("place_id", ""),
            name=place_data.get("name", ""),
            status=place_data.get("business_status", ""),
            address=place_data.get("formatted_address", ""),
            street_number=addr["street_number"],
            street_name=addr["street_name"],
            neighborhood=addr["neighborhood"],
            city=addr["city"],
            state=addr["state"],
            postal_code=addr["postal_code"],
            country=addr["country"],
            lat=location.get("lat", 0.0),
            lng=location.get("lng", 0.0),
            phone=place_data.get("formatted_phone_number", ""),
            international_phone=place_data.get("international_phone_number", ""),
            website=website,
            google_maps_url=place_data.get("url", ""),
            google_maps_direction_url=f"https://www.google.com/maps/dir/?api=1&destination={location.get('lat', '')},{location.get('lng', '')}",
            types=types,
            primary_type=primary_type,
            rating=place_data.get("rating", 0.0),
            total_reviews=place_data.get("user_ratings_total", 0),
            price_level=place_data.get("price_level"),
            reviews=reviews,
            business_hours=opening_hours,
            is_open_now=opening_hours.get("open_now"),
            saturday_hours="",
            sunday_hours="",
            photos=photos,
            photo_count=len(photos),
            editorial_summary=place_data.get("editorial_summary", {}).get(
                "overview", ""
            )
            if place_data.get("editorial_summary")
            else "",
            wheelchair_accessible=place_data.get("wheelchair_accessible_entrance"),
            serves_beer=place_data.get("serves_beer"),
            serves_wine=place_data.get("serves_wine"),
            serves_vegetarian=place_data.get("serves_vegetarian_food"),
            takeout=place_data.get("takeout"),
            delivery=place_data.get("delivery"),
            dine_in=place_data.get("dine_in"),
            curbside_pickup=place_data.get("curbside_pickup"),
            reservable=place_data.get("reservable"),
            serves_breakfast=place_data.get("serves_breakfast"),
            serves_lunch=place_data.get("serves_lunch"),
            serves_dinner=place_data.get("serves_dinner"),
            serves_brunch=place_data.get("serves_brunch"),
            has_website=bool(website),
            icon=place_data.get("icon", ""),
        )
