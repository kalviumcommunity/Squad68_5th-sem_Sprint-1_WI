import streamlit as st
from pathlib import Path

# Imports views directly
from src.views.main_dashboard import render_main_dashboard
from src.views.funnel_deep_dive import render_funnel_deep_dive

# Page Config
st.set_page_config(
    page_title="LearnInsight AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Global CSS Stylesheet
css_path = Path(__file__).parent / "assets" / "css" / "custom.css"
if css_path.exists():
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Placeholder functions for future implementations
def render_course_creator():
    st.title("📖 Course Creator Detail")
    st.info("Course Creator analytics view is coming soon.")

def render_ml_simulator():
    st.title("🧪 ML Simulator")
    st.info("ML Enrollment Prediction & Scenario Simulator view is coming soon.")

# Top Sidebar Header Branding
st.sidebar.markdown("""
<div class="sidebar-brand-container">
    <h2 class="sidebar-brand-title">LearnInsight AI</h2>
    <span class="sidebar-brand-subtitle">v1.0.0</span>
</div>
""", unsafe_allow_html=True)

# Navigation Definition
pages = {
    "Analytics": [
        st.Page(render_main_dashboard, title="Main Dashboard", icon="🎛️"),
        st.Page(render_funnel_deep_dive, title="Funnel Deep-Dive", icon="🔻"),
        st.Page(render_course_creator, title="Course Creator Detail", icon="📖"),
    ],
    "AI Models": [
        st.Page(render_ml_simulator, title="ML Simulator", icon="🧪"),
    ]
}

pg = st.navigation(pages)
pg.run()