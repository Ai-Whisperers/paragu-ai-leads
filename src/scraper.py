import logging
import math
from datetime import datetime
from typing import Optional

from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)
from rich.live import Live
from rich.table import Table
from rich.panel import Panel

from src.config import (
    ASUNCION_BOUNDS,
    GREATER_ASUNCION_BOUNDS,
    SEARCH_RADIUS,
    GRID_STEP,
    GOOGLE_PLACE_TYPES,
)
from src.api_client import PlacesClient
from src.models import Business

logger = logging.getLogger(__name__)
console = Console()


class GridScraper:
    def __init__(self, client: PlacesClient, greater_area: bool = False):
        self.client = client
        self.businesses: dict[str, Business] = {}
        self.bounds = GREATER_ASUNCION_BOUNDS if greater_area else ASUNCION_BOUNDS
        self.errors: list[str] = []

    def generate_grid_points(self) -> list[tuple[float, float]]:
        step = GRID_STEP
        points = []
        lat = self.bounds["south"]
        while lat <= self.bounds["north"]:
            lng = self.bounds["west"]
            while lng <= self.bounds["east"]:
                points.append((round(lat, 5), round(lng, 5)))
                lng += step
            lat += step
        return points

    def scrape_all(
        self,
        place_types: Optional[list[str]] = None,
        include_reviews: bool = True,
        max_pages: int = 3,
    ) -> list[Business]:
        points = self.generate_grid_points()
        total_points = len(points)

        console.print(
            f"\n[bold cyan]Grid Coverage:[/bold cyan] {total_points} search points"
        )
        console.print(
            f"[bold cyan]Area:[/bold cyan] {self.bounds['south']},{self.bounds['west']} → {self.bounds['north']},{self.bounds['east']}"
        )
        console.print(
            f"[bold cyan]Radius:[/bold cyan] {SEARCH_RADIUS}m | [bold cyan]Step:[/bold cyan] {GRID_STEP}°\n"
        )

        types_to_search = place_types if place_types else [None]

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("({task.completed}/{task.total})"),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            main_task = progress.add_task(
                "Scraping grid...", total=total_points * len(types_to_search)
            )

            for place_type in types_to_search:
                type_label = place_type or "all"
                progress.console.print(
                    f"[bold yellow]Searching: {type_label}[/bold yellow]"
                )

                for lat, lng in points:
                    self._scrape_point(lat, lng, place_type, include_reviews, max_pages)
                    progress.advance(main_task)

                progress.console.print(
                    f"  Found so far: [green]{len(self.businesses)}[/green] unique businesses"
                )

        console.print(
            f"\n[bold green]Done![/bold green] Total unique businesses: {len(self.businesses)}"
        )
        console.print(f"[dim]Total API requests: {self.client.requests_count}[/dim]")
        return list(self.businesses.values())

    def _scrape_point(
        self,
        lat: float,
        lng: float,
        place_type: Optional[str],
        include_reviews: bool,
        max_pages: int,
    ):
        page_token = None
        pages = 0

        while pages < max_pages:
            places, next_token = self.client.nearby_search(
                lat=lat,
                lng=lng,
                radius=SEARCH_RADIUS,
                place_type=place_type,
                page_token=page_token,
            )

            for place in places:
                pid = place.get("place_id", "")
                if pid in self.businesses:
                    continue

                details = self.client.get_place_details(pid)
                if not details:
                    continue

                business = self.client.parse_place(
                    details, include_reviews=include_reviews
                )
                business.scraped_at = datetime.now().isoformat()

                self.businesses[pid] = business

            page_token = next_token
            pages += 1

            if not page_token:
                break

    def scrape_neighborhood(
        self,
        neighborhood_name: str,
        center: tuple[float, float],
        radius: int = 1500,
        include_reviews: bool = True,
    ) -> list[Business]:
        console.print(
            f"\n[bold cyan]Scraping neighborhood:[/bold cyan] {neighborhood_name}"
        )
        lat, lng = center
        points = []
        step = GRID_STEP
        for dlat in [-step, 0, step]:
            for dlng in [-step, 0, step]:
                points.append((lat + dlat, lng + dlng))

        for pt_lat, pt_lng in points:
            self._scrape_point(pt_lat, pt_lng, None, include_reviews, max_pages=3)

        found = [
            b
            for b in self.businesses.values()
            if self._point_in_radius(b.lat, b.lng, lat, lng, radius)
        ]
        console.print(
            f"  Found: [green]{len(found)}[/green] businesses in {neighborhood_name}"
        )
        return found

    @staticmethod
    def _point_in_radius(lat1, lng1, lat2, lng2, radius_m):
        R = 6371000
        dlat = math.radians(lat2 - lat1)
        dlng = math.radians(lng2 - lng1)
        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(math.radians(lat1))
            * math.cos(math.radians(lat2))
            * math.sin(dlng / 2) ** 2
        )
        c = 2 * math.asin(math.sqrt(a))
        return R * c <= radius_m
