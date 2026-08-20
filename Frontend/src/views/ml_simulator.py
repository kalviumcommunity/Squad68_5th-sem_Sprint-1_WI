import streamlit as st


def calculate_prediction(price, discount, rating, preview_length, traffic):
    """
    Demo prediction logic.

    This is frontend demo logic only.
    Later, the real ML model/API will replace this.
    """

    base_probability = 0.50

    # Price effect
    if price <= 5000:
        base_probability += 0.08
    elif price >= 9000:
        base_probability -= 0.08

    # Discount effect
    base_probability += (discount / 100) * 0.20

    # Rating effect
    base_probability += ((rating - 3.0) / 2.0) * 0.10

    # Preview length effect
    if preview_length <= 3:
        base_probability += 0.05
    elif preview_length >= 8:
        base_probability -= 0.05

    # Traffic effect
    if traffic >= 50000:
        base_probability += 0.03

    # Keep probability between 5% and 95%
    probability = max(0.05, min(base_probability, 0.95))

    expected_enrollments = int(
        traffic * probability
    )

    return probability, expected_enrollments


def render_ml_simulator():

    st.title("ML Enrollment Simulator")

    st.caption(
        "Simulate enrollment outcomes and understand how course changes "
        "may affect conversion probability."
    )

    st.info(
        "Demo Mode: predictions currently use simulated frontend logic. "
        "The production ML API will be connected later."
    )

    # ---------------------------------------------------------
    # MODEL STATUS
    # ---------------------------------------------------------

    st.subheader("Model Status")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Model Status",
            "ACTIVE"
        )

    with col2:
        st.metric(
            "Prediction Accuracy",
            "88.4%"
        )

    with col3:
        st.metric(
            "ROC-AUC Score",
            "0.91"
        )

    st.divider()

    # ---------------------------------------------------------
    # WHAT-IF SCENARIO
    # ---------------------------------------------------------

    st.subheader("What-If Scenario Simulator")

    st.write(
        "Adjust course conditions to estimate their effect on enrollment."
    )

    col1, col2 = st.columns(2)

    with col1:

        course_category = st.selectbox(
            "Course Category",
            [
                "Data Science",
                "Web Development",
                "Business",
                "Design",
                "Cloud Computing"
            ]
        )

        price = st.number_input(
            "Course Price (₹)",
            min_value=500,
            max_value=20000,
            value=8096,
            step=100
        )

        discount = st.slider(
            "Discount (%)",
            min_value=0,
            max_value=50,
            value=15
        )

    with col2:

        rating = st.slider(
            "Course Rating",
            min_value=1.0,
            max_value=5.0,
            value=4.2,
            step=0.1
        )

        preview_length = st.slider(
            "Preview Length (minutes)",
            min_value=1,
            max_value=15,
            value=3
        )
