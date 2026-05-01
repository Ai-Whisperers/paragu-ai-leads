import json
import logging
from datetime import datetime
from pathlib import Path

import pandas as pd

from src.models import Business, Review

logger = logging.getLogger(__name__)


class Exporter:
    def __init__(self, output_dir: str = "data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _business_to_row(self, b: Business) -> dict:
        return {
            "place_id": b.place_id,
            "name": b.name,
            "status": b.status,
            "address": b.address,
            "street_number": b.street_number,
            "street_name": b.street_name,
            "neighborhood": b.neighborhood,
            "city": b.city,
            "state": b.state,
            "postal_code": b.postal_code,
            "country": b.country,
            "lat": b.lat,
            "lng": b.lng,
            "phone": b.phone,
            "international_phone": b.international_phone,
            "website": b.website,
            "google_maps_url": b.google_maps_url,
            "google_maps_direction_url": b.google_maps_direction_url,
            "types": "|".join(b.types),
            "primary_type": b.primary_type,
            "vertical": b.vertical,
            "rating": b.rating,
            "total_reviews": b.total_reviews,
            "price_level": b.price_level,
            "is_open_now": b.is_open_now,
            "saturday_hours": b.saturday_hours,
            "sunday_hours": b.sunday_hours,
            "photo_count": b.photo_count,
            "editorial_summary": b.editorial_summary,
            "wheelchair_accessible": b.wheelchair_accessible,
            "takeout": b.takeout,
            "delivery": b.delivery,
            "dine_in": b.dine_in,
            "curbside_pickup": b.curbside_pickup,
            "reservable": b.reservable,
            "good_for_children": b.good_for_children,
            "good_for_groups": b.good_for_groups,
            "outdoor_seating": b.outdoor_seating,
            "live_music": b.live_music,
            "serves_beer": b.serves_beer,
            "serves_wine": b.serves_wine,
            "serves_vegan": b.serves_vegan,
            "serves_vegetarian": b.serves_vegetarian,
            "serves_breakfast": b.serves_breakfast,
            "serves_lunch": b.serves_lunch,
            "serves_dinner": b.serves_dinner,
            "serves_brunch": b.serves_brunch,
            "parking_options": "|".join(b.parking_options),
            "payment_options": "|".join(b.payment_options),
            "has_website": b.has_website,
            "website_status": b.website_status,
            "website_is_social_only": b.website_is_social_only,
            "website_is_free_builder": b.website_is_free_builder,
            "website_uses_https": b.website_uses_https,
            "website_redirects_to_social": b.website_redirects_to_social,
            "lead_score": b.lead_score,
            "lead_priority": b.lead_priority,
            "scraped_at": b.scraped_at,
        }

    def _review_to_row(self, b: Business, r: Review) -> dict:
        return {
            "place_id": b.place_id,
            "business_name": b.name,
            "author_name": r.author_name,
            "author_url": r.author_url,
            "rating": r.rating,
            "language": r.language,
            "text": r.text,
            "relative_time": r.relative_time_description,
            "time": r.time,
        }

    def export_all(
        self, businesses: list[Business], summary: dict, tag: str = ""
    ) -> dict[str, str]:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        prefix = f"asuncion_{tag}_" if tag else "asuncion_"

        files = {}

        files["csv_all"] = self._export_csv(
            businesses, f"{prefix}all_businesses_{ts}.csv"
        )
        files["csv_leads"] = self._export_csv(
            [b for b in businesses if b.lead_priority in ("HIGH", "MEDIUM")],
            f"{prefix}leads_{ts}.csv",
        )
        files["csv_no_website"] = self._export_csv(
            [b for b in businesses if not b.has_website or b.website_is_social_only],
            f"{prefix}no_website_{ts}.csv",
        )

        files["reviews_csv"] = self._export_reviews_csv(
            businesses, f"{prefix}reviews_{ts}.csv"
        )

        files["excel"] = self._export_excel(
            businesses, summary, f"{prefix}full_report_{ts}.xlsx"
        )

        files["summary"] = self._export_summary_json(
            summary, f"{prefix}summary_{ts}.json"
        )

        return files

    def _export_csv(self, businesses: list[Business], filename: str) -> str:
        path = self.output_dir / filename
        rows = [self._business_to_row(b) for b in businesses]
        df = pd.DataFrame(rows)
        df.to_csv(path, index=False, encoding="utf-8-sig")
        logger.info(f"Exported {len(rows)} rows to {path}")
        return str(path)

    def _export_reviews_csv(self, businesses: list[Business], filename: str) -> str:
        path = self.output_dir / filename
        rows = []
        for b in businesses:
            for r in b.reviews:
                rows.append(self._review_to_row(b, r))
        df = pd.DataFrame(rows)
        df.to_csv(path, index=False, encoding="utf-8-sig")
        logger.info(f"Exported {len(rows)} reviews to {path}")
        return str(path)

    def _export_excel(
        self, businesses: list[Business], summary: dict, filename: str
    ) -> str:
        path = self.output_dir / filename

        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            all_rows = [self._business_to_row(b) for b in businesses]
            df_all = pd.DataFrame(all_rows)
            df_all.to_excel(writer, sheet_name="All Businesses", index=False)

            leads = [b for b in businesses if b.lead_priority in ("HIGH", "MEDIUM")]
            leads_rows = [
                self._business_to_row(b)
                for b in sorted(leads, key=lambda x: x.lead_score, reverse=True)
            ]
            df_leads = pd.DataFrame(leads_rows)
            df_leads.to_excel(writer, sheet_name="Leads (High+Medium)", index=False)

            no_web = [b for b in businesses if not b.has_website]
            df_no_web = pd.DataFrame([self._business_to_row(b) for b in no_web])
            df_no_web.to_excel(writer, sheet_name="No Website", index=False)

            social_only = [
                b
                for b in businesses
                if b.website_is_social_only or b.website_redirects_to_social
            ]
            df_social = pd.DataFrame([self._business_to_row(b) for b in social_only])
            df_social.to_excel(writer, sheet_name="Social Media Only", index=False)

            review_rows = []
            for b in businesses:
                for r in b.reviews:
                    review_rows.append(self._review_to_row(b, r))
            df_reviews = pd.DataFrame(review_rows)
            df_reviews.to_excel(writer, sheet_name="Reviews", index=False)

            if summary.get("by_vertical"):
                df_vert = pd.DataFrame(
                    list(summary["by_vertical"].items()),
                    columns=["Vertical", "Count"],
                )
                df_vert.to_excel(writer, sheet_name="By Vertical", index=False)

            if summary.get("by_type_top20"):
                df_types = pd.DataFrame(
                    list(summary["by_type_top20"].items()),
                    columns=["Business Type", "Count"],
                )
                df_types.to_excel(writer, sheet_name="Top Types", index=False)

            if summary.get("by_neighborhood"):
                df_neigh = pd.DataFrame(
                    list(summary["by_neighborhood"].items()),
                    columns=["Neighborhood", "Count"],
                )
                df_neigh.to_excel(writer, sheet_name="By Neighborhood", index=False)

            summary_rows = [
                ("Total Businesses", summary.get("total_businesses", 0)),
                ("Average Rating", summary.get("avg_rating", 0)),
                ("Total Reviews (sum)", summary.get("total_reviews_sum", 0)),
                (
                    "No Website",
                    summary.get("website_analysis", {}).get("no_website", 0),
                ),
                (
                    "% No Website",
                    f"{summary.get('website_analysis', {}).get('pct_no_website', 0)}%",
                ),
                (
                    "Social Media Only",
                    summary.get("website_analysis", {}).get("social_media_only", 0),
                ),
                (
                    "Free Builder",
                    summary.get("website_analysis", {}).get("free_builder_site", 0),
                ),
                (
                    "Unreachable/Broken",
                    summary.get("website_analysis", {}).get("unreachable_or_broken", 0),
                ),
                (
                    "HIGH Priority Leads",
                    summary.get("leads", {}).get("high_priority", 0),
                ),
                (
                    "MEDIUM Priority Leads",
                    summary.get("leads", {}).get("medium_priority", 0),
                ),
            ]
            df_summary = pd.DataFrame(summary_rows, columns=["Metric", "Value"])
            df_summary.to_excel(writer, sheet_name="Summary", index=False)

        logger.info(f"Exported Excel report to {path}")
        return str(path)

    def _export_summary_json(self, summary: dict, filename: str) -> str:
        path = self.output_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False, default=str)
        return str(path)
