import pandas as pd


def calculate_retention(preview_data, course_id):

    course_data = preview_data[
        preview_data["course_id"] == course_id
    ].copy()

    if course_data.empty:
        return None

    initial_viewers = course_data.iloc[0]["viewers"]

    course_data["retention"] = (
        course_data["viewers"] / initial_viewers
    ) * 100

    course_data["drop"] = (
        course_data["retention"].shift(1)
        - course_data["retention"]
    )

    return course_data


def find_sharp_dropoff(retention_data, threshold=20):

    sharp_dropoffs = retention_data[
        retention_data["drop"] >= threshold
    ]

    return sharp_dropoffs