import logging
from collections import Counter
from datetime import datetime
from urllib.parse import urlparse

import requests as http_requests

from src.config import (
    VERTICAL_MAPPING,
    META_TYPES,
    DEFAULT_VERTICAL,
    SOCIAL_MEDIA_DOMAINS,
    FREE_WEBSITE_DOMAINS,
    NEIGHBORHOODS_ASUNCION,
)
from src.models import Business

logger = logging.getLogger(__name__)

_TYPE_TO_VERTICAL = {
    t: vertical
    for vertical, vtypes in VERTICAL_MAPPING.items()
    for t in vtypes
}


class BusinessAnalyzer:
    def __init__(self, businesses: list[Business]):
        self.businesses = businesses

    def analyze_all(self, check_websites: bool = True) -> list[Business]:
        for b in self.businesses:
            self._assign_vertical(b)
            self._assign_nearest_neighborhood(b)
            self._compute_hours(b)
            if check_websites:
                self._analyze_website(b)
            self._compute_lead_score(b)
        return self.businesses

    @staticmethod
    def _assign_vertical(business: Business):
        for t in business.types:
            if t in META_TYPES:
                continue
            vertical = _TYPE_TO_VERTICAL.get(t)
            if vertical:
                business.vertical = vertical
                return
        business.vertical = DEFAULT_VERTICAL

    @staticmethod
    def _assign_nearest_neighborhood(business: Business):
        import math

        min_dist = float("inf")
        nearest = "Unknown"
        blat, blng = business.lat, business.lng

        for name, (nlat, nlng) in NEIGHBORHOODS_ASUNCION.items():
            d = math.sqrt((blat - nlat) ** 2 + (blng - nlng) ** 2)
            if d < min_dist:
                min_dist = d
                nearest = name
        business.neighborhood = nearest

    @staticmethod
    def _compute_hours(business: Business):
        weekday_text = business.business_hours.get("weekday_text", [])
        for line in weekday_text:
            lower = line.lower()
            if lower.startswith("saturday"):
                business.saturday_hours = line
            elif lower.startswith("sunday"):
                business.sunday_hours = line

    def _analyze_website(self, business: Business):
        if not business.website:
            business.has_website = False
            business.website_status = "no_website"
            return

        business.has_website = True
        url = business.website.lower()

        if any(domain in url for domain in SOCIAL_MEDIA_DOMAINS):
            business.website_is_social_only = True
            business.website_status = "social_media_only"
            return

        if any(domain in url for domain in FREE_WEBSITE_DOMAINS):
            business.website_is_free_builder = True
            business.website_status = "free_builder"

        business.website_uses_https = url.startswith("https://")

        try:
            resp = http_requests.head(url, timeout=10, allow_redirects=True)
            final_url = resp.url.lower()

            if any(d in final_url for d in SOCIAL_MEDIA_DOMAINS):
                business.website_redirects_to_social = True
                business.website_status = "redirects_to_social"
            elif not business.website_is_free_builder:
                business.website_status = "active"

            if not business.website_uses_https and resp.url.startswith("https://"):
                business.website_uses_https = True

        except http_requests.exceptions.SSLError:
            business.website_status = "ssl_error"
        except http_requests.exceptions.Timeout:
            business.website_status = "timeout"
        except Exception:
            business.website_status = "unreachable"

    @staticmethod
    def _compute_lead_score(business: Business):
        score = 0

        if not business.has_website:
            score += 40
        elif business.website_is_social_only:
            score += 35
        elif business.website_redirects_to_social:
            score += 30
        elif business.website_is_free_builder:
            score += 20
        elif business.website_status in ("ssl_error", "unreachable", "timeout"):
            score += 25
        elif not business.website_uses_https:
            score += 15

        if business.total_reviews >= 50:
            score += 20
        elif business.total_reviews >= 20:
            score += 15
        elif business.total_reviews >= 5:
            score += 10

        if business.rating >= 4.0:
            score += 15
        elif business.rating >= 3.5:
            score += 10

        if business.status == "OPERATIONAL":
            score += 5

        if business.phone:
            score += 5

        business.lead_score = min(score, 100)

        if score >= 60:
            business.lead_priority = "HIGH"
        elif score >= 35:
            business.lead_priority = "MEDIUM"
        else:
            business.lead_priority = "LOW"

    def get_summary(self) -> dict:
        total = len(self.businesses)
        if total == 0:
            return {"total": 0}

        vertical_counts = Counter(b.vertical for b in self.businesses)
        no_website = sum(1 for b in self.businesses if not b.has_website)
        social_only = sum(1 for b in self.businesses if b.website_is_social_only)
        free_builder = sum(1 for b in self.businesses if b.website_is_free_builder)
        unreachable = sum(
            1
            for b in self.businesses
            if b.website_status in ("unreachable", "ssl_error", "timeout")
        )
        redirects_social = sum(
            1 for b in self.businesses if b.website_redirects_to_social
        )

        high_leads = sum(1 for b in self.businesses if b.lead_priority == "HIGH")
        medium_leads = sum(1 for b in self.businesses if b.lead_priority == "MEDIUM")

        avg_rating = sum(b.rating for b in self.businesses) / total
        type_counts = Counter(b.primary_type for b in self.businesses)
        neighborhood_counts = Counter(b.neighborhood for b in self.businesses)

        return {
            "total_businesses": total,
            "by_vertical": dict(vertical_counts.most_common()),
            "by_type_top20": dict(type_counts.most_common(20)),
            "by_neighborhood": dict(neighborhood_counts.most_common()),
            "website_analysis": {
                "no_website": no_website,
                "social_media_only": social_only,
                "free_builder_site": free_builder,
                "unreachable_or_broken": unreachable,
                "redirects_to_social": redirects_social,
                "has_working_website": total
                - no_website
                - social_only
                - free_builder
                - unreachable,
                "pct_no_website": round(no_website / total * 100, 1) if total else 0,
            },
            "leads": {
                "high_priority": high_leads,
                "medium_priority": medium_leads,
                "total_potential_leads": high_leads + medium_leads,
            },
            "avg_rating": round(avg_rating, 2),
            "total_reviews_sum": sum(b.total_reviews for b in self.businesses),
        }

    def get_high_priority_leads(self) -> list[Business]:
        return sorted(
            [b for b in self.businesses if b.lead_priority == "HIGH"],
            key=lambda b: b.lead_score,
            reverse=True,
        )

    def get_by_vertical(self, vertical: str) -> list[Business]:
        return [b for b in self.businesses if b.vertical == vertical]

    def get_by_neighborhood(self, neighborhood: str) -> list[Business]:
        return [b for b in self.businesses if b.neighborhood == neighborhood]

    def get_no_website_businesses(self) -> list[Business]:
        return [b for b in self.businesses if not b.has_website]
