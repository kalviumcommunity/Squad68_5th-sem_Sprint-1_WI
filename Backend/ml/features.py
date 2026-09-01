import pandas as pd


def create_features(courses):

    features = courses.copy()

    features["conversion_rate"] = (
        features["enrollments"]
        / features["views"]
    ) * 100

    features["preview_click_rate"] = (
        features["preview_clicks"]
        / features["views"]
    ) * 100

    features["review_score"] = (
        features["rating"]
        * features["reviews"]
    )

    return features