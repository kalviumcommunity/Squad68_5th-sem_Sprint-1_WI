import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def train_conversion_model(feature_data):

    data = feature_data.copy()

    # Create target
    data["low_conversion"] = (
        data["conversion_rate"] < 5
    ).astype(int)

    feature_columns = [
        "views",
        "preview_clicks",
        "price",
        "rating",
        "reviews",
        "preview_click_rate",
        "review_score"
    ]

    X = data[feature_columns]
    y = data["low_conversion"]

    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    model.fit(X, y)

    data["prediction"] = model.predict(X)

    return model, data