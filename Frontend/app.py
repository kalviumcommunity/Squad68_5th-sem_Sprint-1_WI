import streamlit as st
from pathlib import Path

# Existing pages
from src.views.main_dashboard import render_main_dashboard
from src.views.funnel_deep_dive import render_funnel_deep_dive

# Your new pages
from src.views.ml_simulator import render_ml_simulator
from src.views.course_creator import render_course_creator


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="LearnInsight AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# LOAD GLOBAL CSS
# =========================================================

css_path = Path(__file__).parent / "assets" / "css" / "custom.css"

if css_path.exists():
    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# =========================================================
# SIDEBAR BRANDING
# =========================================================

st.sidebar.markdown(
    """
    <div class="sidebar-brand-container">
        <h2 class="sidebar-brand-title">LearnInsight AI</h2>
        <span class="sidebar-brand-subtitle">v1.0.0</span>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

pages = {
    "Analytics": [
        st.Page(
            render_main_dashboard,
            title="Main Dashboard",
            icon="🎛️"
        ),

        st.Page(
            render_funnel_deep_dive,
            title="Funnel Deep-Dive",
            icon="🔻"
        ),

        st.Page(
            render_course_creator,
            title="Course Creator Detail",
            icon="📖"
        ),
    ],

    "AI Models": [
        st.Page(
            render_ml_simulator,
            title="ML Simulator",
            icon="🧪"
        ),
    ]
}


# =========================================================
# RUN APPLICATION
# =========================================================

pg = st.navigation(pages)

pg.run()