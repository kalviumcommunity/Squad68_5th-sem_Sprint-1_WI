import preprocessing.data_loader as data_loader
import analytics.funnel as funnel
import analytics.retention as retention
import visualization.retention_chart as retention_chart
import analytics.content_match as content_match
import insights.diagnosis as diagnosis


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

    course = courses.iloc[0]

    print("\nSelected Course:")
    print(course["title"])

    funnel_data = funnel.calculate_funnel(course)

    print("\nFunnel Analysis:")

    print(f"Course Views: {funnel_data['course_views']}")
    print(f"Preview Clicks: {funnel_data['preview_clicks']}")
    print(f"Enrollments: {funnel_data['enrollments']}")
    print(f"Conversion Rate: {funnel_data['conversion_rate']:.2f}%")

    retention_data = retention.calculate_retention(
        preview_events,
        course["course_id"]
    )

    print("\nPreview Retention:")

    print(
        retention_data[
            ["video_second", "viewers", "retention"]
        ]
    )

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
                f"{row['drop']:.2f} percentage point drop"
            )

    retention_chart.create_retention_chart(
        retention_data,
        course["title"]
    )

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

    print("\nDiagnosis:")

    for insight in diagnosis_result["diagnosis"]:

        print(f"- {insight}")