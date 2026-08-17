def calculate_funnel(course):

    views = course["views"]
    preview_clicks = course["preview_clicks"]
    enrollments = course["enrollments"]

    if views > 0:
        conversion_rate = (enrollments / views) * 100
    else:
        conversion_rate = 0

    funnel = {
        "course_views": views,
        "preview_clicks": preview_clicks,
        "enrollments": enrollments,
        "conversion_rate": conversion_rate
    }

    return funnel