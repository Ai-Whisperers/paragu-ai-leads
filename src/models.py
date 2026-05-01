from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Review:
    author_name: str = ""
    author_url: str = ""
    language: str = ""
    profile_photo_url: str = ""
    rating: int = 0
    relative_time_description: str = ""
    text: str = ""
    time: int = 0


@dataclass
class Business:
    place_id: str = ""
    name: str = ""
    status: str = ""

    address: str = ""
    street_number: str = ""
    street_name: str = ""
    neighborhood: str = ""
    city: str = ""
    state: str = ""
    postal_code: str = ""
    country: str = ""

    lat: float = 0.0
    lng: float = 0.0

    phone: str = ""
    international_phone: str = ""
    website: str = ""
    google_maps_url: str = ""
    google_maps_direction_url: str = ""

    types: list[str] = field(default_factory=list)
    primary_type: str = ""
    vertical: str = ""
    sub_vertical: str = ""

    rating: float = 0.0
    total_reviews: int = 0
    price_level: Optional[int] = None

    reviews: list[Review] = field(default_factory=list)

    business_hours: dict = field(default_factory=dict)
    is_open_now: Optional[bool] = None
    saturday_hours: str = ""
    sunday_hours: str = ""

    photos: list[str] = field(default_factory=list)
    photo_count: int = 0

    editorial_summary: str = ""
    wheelchair_accessible: Optional[bool] = None
    serves_beer: Optional[bool] = None
    serves_wine: Optional[bool] = None
    serves_vegan: Optional[bool] = None
    serves_vegetarian: Optional[bool] = None
    takeout: Optional[bool] = None
    delivery: Optional[bool] = None
    dine_in: Optional[bool] = None
    curbside_pickup: Optional[bool] = None
    reservable: Optional[bool] = None
    good_for_children: Optional[bool] = None
    good_for_groups: Optional[bool] = None
    outdoor_seating: Optional[bool] = None
    live_music: Optional[bool] = None
    menu_for_children: Optional[bool] = None
    serves_breakfast: Optional[bool] = None
    serves_lunch: Optional[bool] = None
    serves_dinner: Optional[bool] = None
    serves_brunch: Optional[bool] = None
    parking_options: list[str] = field(default_factory=list)
    payment_options: list[str] = field(default_factory=list)
    bathroom: Optional[bool] = None

    has_website: bool = False
    website_status: str = ""
    website_is_social_only: bool = False
    website_is_free_builder: bool = False
    website_uses_https: bool = False
    website_redirects_to_social: bool = False
    lead_score: int = 0
    lead_priority: str = ""

    icon: str = ""
    icon_bg_color: str = ""

    scraped_at: str = ""
