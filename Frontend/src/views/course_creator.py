import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def render_course_creator():

    # =========================================================
    # PAGE HEADER
    # =========================================================

    st.title("Course Creator Detail")

    st.write(
        "Analyze course performance, learner behavior, and enrollment conversion."
    )

    # =========================================================
    # TOP CONTROLS
    # =========================================================

    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        course = st.selectbox(
            "Select Course",
            [
                "Advanced Digital Marketing Strategy",
                "Intro to Machine Learning Models",
                "Cloud Computing Recovery",
                "UI/UX Fundamentals Workshop",
            ],
        )

    with col2:
        date_range = st.selectbox(
            "Date Range",
            [
                "Last 30 Days",
                "Last 90 Days",
                "Last 6 Months",
                "Last 12 Months",
            ],
        )

    with col3:
        st.write("")
        st.write("")
        if st.button("Export Report"):
            st.success("Report ready for export.")


    # =========================================================
    # COURSE INFORMATION
    # =========================================================

    st.markdown("---")

    st.subheader(course)

    info1, info2, info3, info4 = st.columns(4)

    with info1:
        st.metric(
            "Category",
            "Marketing" if "Marketing" in course else "Technology"
        )

    with info2:
        st.metric(
            "Instructor",
            "Neha Verma"
        )

    with info3:
        st.metric(
            "Course Price",
            "₹8,569"
        )

    with info4:
        st.metric(
            "Status",
            "Published"
        )


    # =========================================================
    # COURSE PERFORMANCE KPIs
    # =========================================================

    st.markdown("### Course Performance")

    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    with kpi1:
        st.metric(
            "Views",
            "24.5k",
            "+8.2%"
        )

    with kpi2:
        st.metric(
            "Preview Clicks",
            "8.9k",
            "+4.6%"
        )

    with kpi3:
        st.metric(
            "Cart Adds",
            "1.7k",
            "-3.2%"
        )

    with kpi4:
        st.metric(
            "Enrollments",
            "560",
            "+12.4%"
        )

    with kpi5:
        st.metric(
            "Conversion Rate",
            "3.2%",
            "+1.2%"
        )


    # =========================================================
    # COURSE HEALTH SCORE
    # =========================================================

    st.markdown("### Course Health")

    health_col1, health_col2 = st.columns([1, 2])

    with health_col1:

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=82,
                title={"text": "Health Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "threshold": {
                        "line": {"width": 4},
                        "value": 70,
                        },
                        },
                        )
                        )

        fig.update_layout(
            height=280,
            margin=dict(l=20, r=20, t=60, b=20),
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with health_col2:

        st.markdown("#### Health Score Factors")

        st.success("✓ Strong search volume")

        st.success("✓ Above-average preview engagement")

        st.warning("⚠ Low preview-to-cart conversion")

        st.warning("⚠ Price friction detected")

        st.info("ℹ Course rating is performing well")


    # =========================================================
    # ENROLLMENT FUNNEL
    # =========================================================

    st.markdown("### Enrollment Funnel")

    funnel_data = {
        "Stage": [
            "Search",
            "Preview",
            "Cart",
            "Checkout",
            "Enrollment",
        ],
        "Users": [
            24500,
            8900,
            1700,
            920,
            560,
        ],
    }

    funnel_df = pd.DataFrame(funnel_data)

    fig = go.Figure(
        go.Funnel(
            y=funnel_df["Stage"],
            x=funnel_df["Users"],
            textinfo="value+percent initial",
        )
    )

    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=30, b=20),
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =========================================================
    # DROP-OFF ANALYSIS
    # =========================================================

    st.markdown("### Funnel Drop-off Analysis")

    drop1, drop2, drop3 = st.columns(3)

    with drop1:

        st.error(
            "68.5% Drop-off"
        )

        st.markdown(
            "**Preview → Cart**"
        )

        st.write(
            "Most learners leave after viewing the course."
        )

    with drop2:

        st.warning(
            "45.9% Drop-off"
        )

        st.markdown(
            "**Cart → Checkout**"
        )

        st.write(
            "Price sensitivity may be affecting purchase intent."
        )
