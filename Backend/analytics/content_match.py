def analyze_content_match(search_data, topic_data, course_id):

    searches = search_data[
        search_data["course_id"] == course_id
    ].copy()

    topics = topic_data[
        topic_data["course_id"] == course_id
    ].copy()

    result = searches.merge(
        topics,
        left_on="search_term",
        right_on="topic",
        how="left"
    )

    result["coverage"] = result["coverage"].fillna(0)

    result["status"] = result["coverage"].apply(
        classify_coverage
    )

    return result


def classify_coverage(coverage):

    if coverage == 0:
        return "Missing"

    elif coverage < 0.75:
        return "Partially Covered"

    else:
        return "Covered"