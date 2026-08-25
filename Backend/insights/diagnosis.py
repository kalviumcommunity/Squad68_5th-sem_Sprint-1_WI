def generate_diagnosis(
    funnel_data,
    retention_data,
    content_data
):

    insights = []

    conversion_rate = funnel_data["conversion_rate"]

    # Check conversion rate
    if conversion_rate < 5:
        insights.append(
            f"Low conversion rate detected: "
            f"{conversion_rate:.2f}%"
        )

    # Check preview drop-off
    if not retention_data.empty:

        sharp_dropoffs = retention_data[
            retention_data["drop"] >= 20
        ]

        for _, row in sharp_dropoffs.iterrows():

            minutes = int(row["video_second"] // 60)
            seconds = int(row["video_second"] % 60)

            insights.append(
                f"Major preview drop-off detected at "
                f"{minutes:02d}:{seconds:02d}"
            )

    # Check missing content
    missing_topics = content_data[
        content_data["status"] == "Missing"
    ]

    for _, row in missing_topics.iterrows():

        insights.append(
            f"High-demand topic '{row['search_term']}' "
            f"is missing from the course"
        )

    return insights