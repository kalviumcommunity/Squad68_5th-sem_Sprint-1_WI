import streamlit as st
import pandas as pd
from src.components.navbar import render_top_navbar

def render_main_dashboard():
    render_top_navbar()
    st.markdown("<br>", unsafe_allow_html=True)
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    with kpi1:
        st.markdown("""
        <div class="css-card">
            <span style="font-size:0.75rem; color:#64748B; font-weight:700;">OVERALL CONVERSION RATE</span>
            <div style="font-size:1.8rem; font-weight:800; margin-top:4px;">14.2% <span class="badge-green">+1.2%</span></div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi2:
        st.markdown("""
        <div class="css-card">
            <span style="font-size:0.75rem; color:#64748B; font-weight:700;">TOTAL PREVIEW CLICKS</span>
            <div style="font-size:1.8rem; font-weight:800; margin-top:4px;">45.2k <span style="font-size:0.8rem; color:#64748B;">vs 42.1k last mo</span></div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi3:
        st.markdown("""
        <div class="css-card">
            <span style="font-size:0.75rem; color:#64748B; font-weight:700;">OVERALL ENROLLMENTS</span>
            <div style="font-size:1.8rem; font-weight:800; margin-top:4px;">6.4k</div>
        </div>
        """, unsafe_allow_html=True)
        
    with kpi4:
        st.markdown("""
        <div class="badge-warning">
            ⚠️ <b>BOTTLENECK WARNING</b><br>
            <b>Preview → Cart</b> has a <b>68.5% Drop-off</b> rate.
        </div>
        """, unsafe_allow_html=True)

    c1, c2 = st.columns([1.3, 1])
    
    with c1:
        st.subheader("Funnel Drop-off Analysis")
        st.markdown("""
        <div class="css-card">
            <div class="list-item"><span>Search</span> <b>120k</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 100%;"></div></div><br>
            <div class="list-item"><span>Preview</span> <b>45.2k</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 38%; background-color:#64748B;"></div></div><br>
            <div class="list-item"><span>Cart Addition <span class="badge-red">High Drop-off</span></span> <b>14.3k</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 12%; background-color:#EF4444;"></div></div><br>
            <div class="list-item"><span>Enrolled</span> <b>6.4k</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 5%; background-color:#1E293B;"></div></div>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.subheader("Top Keywords vs Conv %")
        st.markdown("""
        <div class="css-card">
            <div class="list-item"><span>Data Science</span> <b>5.2%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 80%;"></div></div><br>
            <div class="list-item"><span>UX Design</span> <b>4.8%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 72%;"></div></div><br>
            <div class="list-item"><span>React</span> <b>4.1%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 60%;"></div></div><br>
            <div class="list-item"><span>Python</span> <b>3.9%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 55%;"></div></div><br>
            <div class="list-item"><span>Marketing</span> <b style="color:#EF4444;">2.1%</b></div>
            <div class="progress-bg"><div class="progress-fill" style="width: 30%; background-color:#EF4444;"></div></div>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("High Views / Low Conversion Courses")
    
    table_data = pd.DataFrame({
        "COURSE NAME": ["Advanced Digital Marketing", "Fullstack Web Dev 2026", "Cloud Architecture AWS", "AI & Machine Learning"],
        "CATEGORY": ["Marketing", "Web Dev", "Cloud", "Data Science"],
        "VIEWS": [28400, 19200, 15400, 31000],
        "CONV %": ["1.8%", "2.3%", "1.9%", "3.1%"],
        "ML LIKELIHOOD SCORE": [0.32, 0.45, 0.28, 0.52],
        "PRIMARY DROP-OFF REASON": ["Price point friction at checkout", "Preview length too short", "Missing prerequisite topics", "Syllabus mismatch"],
        "ACTION": ["Inspect", "Inspect", "Inspect", "Inspect"]
    })
    
    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "ML LIKELIHOOD SCORE": st.column_config.ProgressColumn("ML Score", min_value=0, max_value=1, format="%.2f")
        }
    )

render_main_dashboard()