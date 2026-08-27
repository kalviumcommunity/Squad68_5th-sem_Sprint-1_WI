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
    with drop3:

        st.success(
            "39.1% Conversion"
        )

        st.markdown(
            "**Checkout → Enrollment**"
        )

        st.write(
            "Users reaching checkout show strong purchase intent."
        )


    # =========================================================
    # TREND ANALYSIS
    # =========================================================

    st.markdown("### Enrollment Trend")

    trend_data = pd.DataFrame(
        {
            "Week": [
                "Week 1",
                "Week 2",
                "Week 3",
                "Week 4",
                "Week 5",
                "Week 6",
            ],
            "Views": [
                5200,
                6100,
                5800,
                6400,
                5900,
                6800,
            ],
            "Enrollments": [
                92,
                110,
                104,
                128,
                119,
                145,
            ],
        }
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=trend_data["Week"],
            y=trend_data["Views"],
            mode="lines+markers",
            name="Views",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=trend_data["Week"],
            y=trend_data["Enrollments"],
            mode="lines+markers",
            name="Enrollments",
            yaxis="y2",
        )
    )

    fig.update_layout(
        height=400,
        yaxis=dict(
            title="Views"
        ),
        yaxis2=dict(
            title="Enrollments",
            overlaying="y",
            side="right",
        ),
        margin=dict(l=20, r=20, t=30, b=20),
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =========================================================
    # PRIMARY DROP-OFF REASON
    # =========================================================

    st.markdown("### Primary Drop-off Reason")

    reason_col1, reason_col2 = st.columns([1, 2])

    with reason_col1:

        st.error(
            "Price Point Friction"
        )

        st.metric(
            "Estimated Impact",
            "-18%"
        )

    with reason_col2:

        st.markdown(
            """
            **What the data suggests**

            Learners show strong interest in the course through
            search and preview activity, but conversion falls sharply
            when they reach the purchase stage.

            Historical behavior indicates that the current price is
            above the category benchmark.
            """
        )

        st.info(
            "Category benchmark: ₹4,762"
        )


    # =========================================================
    # AI RECOMMENDATIONS
    # =========================================================

    st.markdown("### AI Recommended Actions")

    recommendation1, recommendation2, recommendation3 = st.columns(3)

    with recommendation1:

        st.markdown("#### High Impact")

        st.write(
            "Adjust pricing closer to the category benchmark."
        )

        st.metric(
            "Estimated Conversion Impact",
            "+12.4%"
        )

        if st.button(
            "Review Pricing",
            key="review_pricing"
        ):
            st.info(
                "Recommended price range: ₹4,500 - ₹5,000"
            )

    with recommendation2:

        st.markdown("#### Medium Impact")

        st.write(
            "Shorten the introduction of the preview video."
        )

        st.metric(
            "Potential Drop-off Reduction",
            "18%"
        )

        if st.button(
            "Review Video",
            key="review_video"
        ):
            st.info(
                "Current drop-off occurs around 02:15."
            )

    with recommendation3:

        st.markdown("#### Opportunity")

        st.write(
            "Add a hands-on project preview."
        )

        st.metric(
            "Expected Enrollment Lift",
            "+8%"
        )

        if st.button(
            "Add Project Preview",
            key="add_project"
        ):
            st.info(
                "Upload a project demonstration to improve learner confidence."
            )


    # =========================================================
    # LEARNER SEARCH VS COURSE CONTENT
    # =========================================================

    st.markdown("### Search Intent vs Course Content")

    keyword_data = pd.DataFrame(
        {
            "Search Keyword": [
                "Python",
                "Machine Learning",
                "SQL",
                "Data Science",
                "LLMs",
            ],
            "Search Volume": [
                12000,
                9400,
                6200,
                5800,
                4100,
            ],
            "Content Match": [
                "100%",
                "92%",
                "75%",
                "88%",
                "58%",
            ],
        }
    )

    st.dataframe(
        keyword_data,
        use_container_width=True,
        hide_index=True,
    )


    # =========================================================
    # FINAL INSIGHT
    # =========================================================

    st.markdown("### Overall AI Insight")

    st.info(
        """
        **The course attracts strong learner interest but loses users
        primarily between preview and cart.**

        The biggest opportunity is reducing price friction while
        improving the preview experience. Based on historical
        behavior, these changes could meaningfully improve enrollment
        conversion.
        """
    )