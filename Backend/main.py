import preprocessing.data_loader as data_loader
import analytics.funnel as funnel
import analytics.retention as retention
import visualization.retention_chart as retention_chart
import analytics.content_match as content_match
import insights.diagnosis as diagnosis
import analytics.course_features as course_features
import ml.features as features


courses = data_loader.load_courses()
preview_events = data_loader.load_preview_events()
searches = data_loader.load_searches()
course_topics = data_loader.load_course_topics()


if (
    courses is not None
    and preview_events is not None
    and searches is not None
    and course_topics is not None
):

    # -----------------------------
    # ML FEATURE ENGINEERING
    # -----------------------------

    feature_data = features.create_features(courses)

    print("\nML Features:")

    print(
        feature_data[
            [
                "title",
                "views",
                "preview_clicks",
                "enrollments",
                "price",
                "rating",
                "reviews",
                "conversion_rate",
                "preview_click_rate",
                "review_score"
            ]
        ]
    )


    # -----------------------------
    # SELECT COURSE
    # -----------------------------

    course = courses.iloc[0]

    print("\nSelected Course:")
    print(course["title"])


    # -----------------------------
    # FUNNEL ANALYSIS
    # -----------------------------

    funnel_data = funnel.calculate_funnel(course)

    print("\nFunnel Analysis:")

    print(
        f"Course Views: "
        f"{funnel_data['course_views']}"
    )

    print(
        f"Preview Clicks: "
        f"{funnel_data['preview_clicks']}"
    )

    print(
        f"Enrollments: "
        f"{funnel_data['enrollments']}"
    )

    print(
        f"Conversion Rate: "
        f"{funnel_data['conversion_rate']:.2f}%"
    )


    # -----------------------------
    # PREVIEW RETENTION
    # -----------------------------

    retention_data = retention.calculate_retention(
        preview_events,
        course["course_id"]
    )

    print("\nPreview Retention:")

    print(
        retention_data[
            [
                "video_second",
                "viewers",
                "retention"
            ]
        ]
    )


    # -----------------------------
    # SHARP DROP-OFF DETECTION
    # -----------------------------

    sharp_dropoffs = retention.find_sharp_dropoff(
        retention_data
    )

    print("\nSharp Drop-offs:")

    if sharp_dropoffs.empty:

        print("No sharp drop-off detected.")

    else:

        for _, row in sharp_dropoffs.iterrows():

            print(
                f"At {row['video_second']} seconds: "
                f"{row['drop']:.2f} "
                f"percentage point drop"
            )


    # -----------------------------
    # RETENTION VISUALIZATION
    # -----------------------------

    retention_chart.create_retention_chart(
        retention_data,
        course["title"]
    )


    # -----------------------------
    # CONTENT MATCH ANALYSIS
    # -----------------------------

    content_data = content_match.analyze_content_match(
        searches,
        course_topics,
        course["course_id"]
    )

    print("\nContent Match Analysis:")

    print(
        content_data[
            [
                "search_term",
                "search_count",
                "coverage",
                "status"
            ]
        ]
    )


    # -----------------------------
    # COURSE DIAGNOSIS
    # -----------------------------

    diagnosis_result = diagnosis.generate_diagnosis(
        funnel_data,
        retention_data,
        content_data
    )

    print("\nCourse Health:")

    print(
        f"Conversion Status: "
        f"{diagnosis_result['conversion_status']}"
    )

    print(
        f"Retention Status: "
        f"{diagnosis_result['retention_status']}"
    )


    # -----------------------------
    # CONTENT GAPS
    # -----------------------------

    print("\nContent Gaps:")

    content_gaps = diagnosis_result["content_gaps"]

    if content_gaps.empty:

        print("No missing topics detected.")

    else:

        for _, row in content_gaps.iterrows():

            print(
                f"- {row['search_term']} "
                f"({row['search_count']} searches)"
            )


    # -----------------------------
    # DIAGNOSIS
    # -----------------------------

    print("\nDiagnosis:")

    for insight in diagnosis_result["diagnosis"]:

        print(f"- {insight}")


    # -----------------------------
    # COURSE FEATURES
    # -----------------------------

    preview_completion = (
        course_features.calculate_preview_completion(
            retention_data
        )
    )

    average_watch_time = (
        course_features.calculate_average_watch_time(
            retention_data
        )
    )

    content_match_score = (
        course_features.calculate_content_match(
            content_data
        )
    )

    print("\nCourse Features:")

    print(
        f"Preview Completion Rate: "
        f"{preview_completion:.2f}%"
    )

    print(
        f"Average Preview Watch Time: "
        f"{average_watch_time:.2f} seconds"
    )

    print(
        f"Content Match Score: "
        f"{content_match_score:.2f}%"
    )

    print(
        f"Course Price: "
        f"₹{course['price']}"
    )

    print(
        f"Course Rating: "
        f"{course['rating']}"
    )

    print(
        f"Number of Reviews: "
        f"{course['reviews']}"
    )