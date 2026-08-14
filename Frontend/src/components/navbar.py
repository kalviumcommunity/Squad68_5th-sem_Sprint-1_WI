import streamlit as st

def render_top_navbar():
    col1, col2, col3, col4 = st.columns([2.5, 1, 1, 0.5])
    
    with col1:
        st.text_input("Search...", placeholder="Search courses, users or metrics...", label_visibility="collapsed")
    with col2:
        st.selectbox("Timeframe", ["Last 30 Days", "Last 7 Days", "Quarter to Date"], label_visibility="collapsed")
    with col3:
        if st.button("Export Report", type="primary", use_container_width=True):
            st.toast("Report export initiated!", icon="📥")
    with col4:
        st.write("🔔")