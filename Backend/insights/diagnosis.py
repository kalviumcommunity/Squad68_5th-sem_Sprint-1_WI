def analyze_conversion(conversion_rate):

    if conversion_rate < 5:
        return "Low"

    elif conversion_rate < 10:
        return "Moderate"

    else:
        return "Good"


def analyze_retention(retention_data):

    if retention_data.empty:
        return "No Data"

    average_retention = retention_data["retention"].mean()

    if average_retention < 40:
        return "Critical"

    elif average_retention < 70:
        return "Warning"

    else:
        return "Healthy"


def find_content_gaps(content_data):

    missing_topics = content_data[
        content_data["status"] == "Missing"
    ]

    missing_topics = missing_topics.sort_values(
        by="search_count",
        ascending=False
    )

    return missing_topics


def generate_diagnosis(
    funnel_data,
    retention_data,
    content_data
):

    diagnosis = []

    conversion_rate = funnel_data["conversion_rate"]

    # Conversion analysis
    conversion_status = analyze_conversion(
        conversion_rate
    )

    if conversion_status == "Low":

        diagnosis.append(
            f"Conversion rate is low at "
            f"{conversion_rate:.2f}%."
        )

    # Retention analysis
    retention_status = analyze_retention(
        retention_data
    )

    if retention_status == "Critical":

        diagnosis.append(
            "Preview retention is critically low."
        )

    elif retention_status == "Warning":

        diagnosis.append(
            "Preview retention needs improvement."
        )

    # Sharp drop-off analysis
    sharp_dropoffs = retention_data[
        retention_data["drop"] >= 20
    ]

    for _, row in sharp_dropoffs.iterrows():

        minutes = int(row["video_second"] // 60)
        seconds = int(row["video_second"] % 60)

        diagnosis.append(
            f"Major preview drop-off detected at "
            f"{minutes:02d}:{seconds:02d}."
        )

    # Content gap analysis
    content_gaps = find_content_gaps(
        content_data
    )

    for _, row in content_gaps.iterrows():

        diagnosis.append(
            f"High-demand topic "
            f"'{row['search_term']}' "
            f"is missing from the course."
        )

    return {
        "conversion_status": conversion_status,
        "retention_status": retention_status,
        "content_gaps": content_gaps,
        "diagnosis": diagnosis
    }