import os
import requests
import streamlit as st

# Configurable backend API base URL
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000/api/v1")

@st.cache_data(ttl=60)
def fetch_from_backend(endpoint: str, default_payload: dict):
    """
    Requests data from the backend API.
    Falls back gracefully to default_payload if backend server is unreachable.
    """
    try:
        response = requests.get(f"{BACKEND_URL}/{endpoint}", timeout=3)
        if response.status_code == 200:
            return response.json(), True
    except requests.exceptions.RequestException:
        pass
    return default_payload, False


def get_dashboard_data():
    """Fetch Main Dashboard KPIs, Funnel Analysis, and Course Table."""
    fallback_data = {
        "kpis": {
            "conversion_rate": "14.2%",
            "conversion_change": "+1.2%",
            "preview_clicks": "45.2k",
            "preview_clicks_subtext": "vs 42.1k last mo",
            "enrollments": "6.4k",
            "bottleneck_warning": "<b>Preview → Cart</b> has a <b>68.5% Drop-off</b> rate."
        },
        "funnel_summary": {
            "search": "120k", "search_pct": 100,
            "preview": "45.2k", "preview_pct": 38,
            "cart": "14.3k", "cart_pct": 12,
            "enrolled": "6.4k", "enrolled_pct": 5
        },
        "keywords": [
            {"name": "Data Science", "rate": "5.2%", "pct": 80, "color": "#1E293B"},
            {"name": "UX Design", "rate": "4.8%", "pct": 72, "color": "#1E293B"},
            {"name": "React", "rate": "4.1%", "pct": 60, "color": "#1E293B"},
            {"name": "Python", "rate": "3.9%", "pct": 55, "color": "#1E293B"},
            {"name": "Marketing", "rate": "2.1%", "pct": 30, "color": "#EF4444"}
        ],
        "courses_table": [
            {"COURSE NAME": "Advanced Digital Marketing", "CATEGORY": "Marketing", "VIEWS": 28400, "CONV %": "1.8%", "ML LIKELIHOOD SCORE": 0.32, "PRIMARY DROP-OFF REASON": "Price point friction at checkout", "ACTION": "Inspect"},
            {"COURSE NAME": "Fullstack Web Dev 2026", "CATEGORY": "Web Dev", "VIEWS": 19200, "CONV %": "2.3%", "ML LIKELIHOOD SCORE": 0.45, "PRIMARY DROP-OFF REASON": "Preview length too short", "ACTION": "Inspect"},
            {"COURSE NAME": "Cloud Architecture AWS", "CATEGORY": "Cloud", "VIEWS": 15400, "CONV %": "1.9%", "ML LIKELIHOOD SCORE": 0.28, "PRIMARY DROP-OFF REASON": "Missing prerequisite topics", "ACTION": "Inspect"},
            {"COURSE NAME": "AI & Machine Learning", "CATEGORY": "Data Science", "VIEWS": 31000, "CONV %": "3.1%", "ML LIKELIHOOD SCORE": 0.52, "PRIMARY DROP-OFF REASON": "Syllabus mismatch", "ACTION": "Inspect"}
        ]
    }
    return fetch_from_backend("dashboard", fallback_data)


def get_funnel_deep_dive_data():
    """Fetch Funnel Deep-Dive breakdown and traffic sources."""
    fallback_data = {
        "metrics": {
            "total_visits": "120,450",
            "preview_rate": "37.5%",
            "preview_rate_badge": "+2.1%",
            "cart_dropoff": "68.5%",
            "checkout_conversion": "44.7%"
        },
        "funnel_steps": [
            {"step": "1. Landing & Search", "count": "120,450", "pct_str": "100%", "width": 100, "color": "#1E293B", "badge": ""},
            {"step": "2. Course Preview Click", "count": "45,200", "pct_str": "37.5%", "width": 37.5, "color": "#6366F1", "badge": ""},
            {"step": "3. Added to Cart", "count": "14,238", "pct_str": "11.8%", "width": 11.8, "color": "#EF4444", "badge": "<span class='badge-red'>Bottleneck</span>"},
            {"step": "4. Initiate Checkout", "count": "9,150", "pct_str": "7.6%", "width": 7.6, "color": "#F59E0B", "badge": ""},
            {"step": "5. Completed Enrollment", "count": "6,400", "pct_str": "5.3%", "width": 5.3, "color": "#10B981", "badge": ""}
        ],
        "category_table": [
            {"CATEGORY": "Data Science", "PREVIEWS": 15200, "CART ADDS": 6100, "ENROLLED": 2800, "CART DROP-OFF %": "59.8%", "PRIMARY FRICTION": "Price sensitivity"},
            {"CATEGORY": "Web Development", "PREVIEWS": 12800, "CART ADDS": 4200, "ENROLLED": 1900, "CART DROP-OFF %": "67.1%", "PRIMARY FRICTION": "Short preview video"},
            {"CATEGORY": "Cloud Computing", "PREVIEWS": 8400, "CART ADDS": 2100, "ENROLLED": 920, "CART DROP-OFF %": "75.0%", "PRIMARY FRICTION": "Missing prerequisites"},
            {"CATEGORY": "UI/UX Design", "PREVIEWS": 5200, "CART ADDS": 1100, "ENROLLED": 480, "CART DROP-OFF %": "78.8%", "PRIMARY FRICTION": "Lack of portfolio examples"},
            {"CATEGORY": "Digital Marketing", "PREVIEWS": 3600, "CART ADDS": 738, "ENROLLED": 300, "CART DROP-OFF %": "79.6%", "PRIMARY FRICTION": "Unclear course outcomes"}
        ]
    }
    return fetch_from_backend("funnel", fallback_data)