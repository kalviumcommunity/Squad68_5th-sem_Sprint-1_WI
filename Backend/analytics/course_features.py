def calculate_preview_completion(retention_data):

    if retention_data.empty:
        return 0

    initial_viewers = retention_data.iloc[0]["viewers"]
    final_viewers = retention_data.iloc[-1]["viewers"]

    if initial_viewers == 0:
        return 0

    completion_rate = (
        final_viewers / initial_viewers
    ) * 100

    return completion_rate


def calculate_average_watch_time(retention_data):

    if retention_data.empty:
        return 0

    total_viewers = retention_data["viewers"].sum()

    if total_viewers == 0:
        return 0

    weighted_time = (
        retention_data["video_second"]
        * retention_data["viewers"]
    ).sum()

    average_watch_time = (
        weighted_time / total_viewers
    )

    return average_watch_time


def calculate_content_match(content_data):

    if content_data.empty:
        return 0

    content_match = (
        content_data["coverage"].mean()
    ) * 100

    return content_match