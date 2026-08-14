import streamlit as st
import pandas as pd
from src.components.navbar import render_top_navbar
from src.api.client import get_funnel_deep_dive_data

def render_funnel_deep_dive():
    render_top_navbar()
    
    data, is_live = get_funnel_deep_dive_data()
    
    if is_live:
        st.caption("🟢 Connected to Live Backend API")
    else:
        st.caption("🟡 Running on Fallback API Data (Backend Offline)")

    st.markdown("<br>", unsafe_allow_html=True)
    st.title("🔻 Funnel Deep-Dive Analysis")
    st.caption("Detailed stage-by-stage drop-off analytics fetched live from the API server.")
    
    # Metrics
    m = data["metrics"]
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown(f"""
        <div class="css-card">
            <span style="font-size:0.75rem; color:#64748B; font-weight:700;">TOTAL VISITS</span>
            <div style="font-size:1.8rem; font-weight:800; margin-top:4px;">{m['total_visits']}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with m2:
        st.markdown(f"""
        <div class="css-card">
            <span style="font-size:0.75rem; color:#64748B; font-weight:700;">PREVIEW RATE</span>
            <div style="font-size:1.8rem; font-weight:800; margin-top:4px;">{m['preview_rate']} <span class="badge-green">{m['preview_rate_badge']}</span></div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="css-card">
            <span style="font-size:0.75rem; color:#64748B; font-weight:700;">CART DROP-OFF</span>
            <div style="font-size:1.8rem; font-weight:800; margin-top:4px; color:#EF4444;">{m['cart_dropoff']} <span class="badge-red">High Friction</span></div>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
        <div class="css-card">
            <span style="font-size:0.75rem; color:#64748B; font-weight:700;">CHECKOUT CONVERSION</span>
            <div style="font-size:1.8rem; font-weight:800; margin-top:4px;">{m['checkout_conversion']}</div>
        </div>
        """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1.2, 1])
    
    with col_left:
        st.subheader("Step-by-Step Conversion Flow")
        step_html = '<div class="css-card">'
        for step in data["funnel_steps"]:
            step_html += f"""
            <div class="list-item">
                <span><b>{step['step']}</b> {step['badge']}</span>
                <span><b>{step['count']}</b> ({step['pct_str']})</span>
            </div>
            <div class="progress-bg"><div class="progress-fill" style="width: {step['width']}%; background-color:{step['color']};"></div></div>
            <br>
            """
        step_html += '</div>'
        st.markdown(step_html, unsafe_allow_html=True)
        
    with col_right:
        st.subheader("Traffic Source Conversion")
        st.markdown("""
        <div class="css-card">
            <div class="list-item"><span>Organic Search</span> <b>6.4%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 65%;"></div></div><br>
            <div class="list-item"><span>Direct / Bookmark</span> <b>8.1%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 81%;"></div></div><br>
            <div class="list-item"><span>Email Campaigns</span> <b>5.2%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 52%;"></div></div><br>
            <div class="list-item"><span>Paid Social Ads</span> <b style="color:#EF4444;">1.9%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 20%; background-color:#EF4444;"></div></div>
        </div>
        """, unsafe_allow_html=True)

    # Category Table
    st.subheader("Category Drop-off Comparison")
    funnel_df = pd.DataFrame(data["category_table"])
    st.dataframe(funnel_df, use_container_width=True, hide_index=True)