"""
=========================================================
LearnInsight AI - Backend API Endpoints
=========================================================

PRODUCTION BASE URL:
https://learninsight-nxuo.onrender.com

API DOCUMENTATION:
https://learninsight-nxuo.onrender.com/docs


AVAILABLE API ENDPOINTS
---------------------------------------------------------

1. Health Check
GET:
https://learninsight-nxuo.onrender.com/

Purpose:
Checks whether the backend API is running.


2. Get All Courses
GET:
https://learninsight-nxuo.onrender.com/api/courses

Purpose:
Returns information about all available courses.


3. Get Course Analysis
GET:
https://learninsight-nxuo.onrender.com/api/courses/{course_id}

Purpose:
Returns complete analysis for a specific course.

Example:
https://learninsight-nxuo.onrender.com/api/courses/101


COURSE ANALYSIS RESPONSE INCLUDES
---------------------------------------------------------

- Course information
- Views
- Preview clicks
- Enrollments
- Conversion rate
- Preview completion rate
- Average preview watch time
- Content match score
- Preview retention data
- Content gaps
- Course health
- ML prediction
- Diagnosis


FOR FRONTEND TEAM
---------------------------------------------------------

Use the PRODUCTION BASE URL to connect the frontend
with the deployed backend.

Example:

GET https://learninsight-nxuo.onrender.com/api/courses

GET https://learninsight-nxuo.onrender.com/api/courses/101

The frontend can use the JSON response to display:

- Dashboard statistics
- Conversion rate
- Course health
- Retention graph
- Content gaps
- ML prediction
- Diagnosis


API DOCUMENTATION
---------------------------------------------------------

Interactive Swagger documentation:

https://learninsight-nxuo.onrender.com/docs


NOTE:
The backend is deployed on Render and is publicly accessible.
The frontend should use the production URLs above instead
of the local URL (http://127.0.0.1:8000).


=========================================================
"""
















from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import preprocessing.data_loader as data_loader
import analytics.funnel as funnel
import analytics.retention as retention
import analytics.content_match as content_match
import insights.diagnosis as diagnosis
import analytics.course_features as course_features
import ml.features as features
import ml.model as model


app = FastAPI(
    title="LearnInsight AI API",
    description="Backend API for course conversion analysis",
    version="1.0"
)


# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load data
courses = data_loader.load_courses()
preview_events = data_loader.load_preview_events()
searches = data_loader.load_searches()
course_topics = data_loader.load_course_topics()


# Create ML features and train model
feature_data = features.create_features(courses)
conversion_model, ml_results = model.train_conversion_model(
    feature_data
)


@app.get("/")
def home():
    return {
        "message": "LearnInsight AI API is running"
    }


@app.get("/api/courses")
def get_courses():

    results = []

    for _, course in courses.iterrows():

        results.append({
            "course_id": int(course["course_id"]),
            "title": course["title"],
            "instructor": course["instructor"],
            "price": float(course["price"]),
            "views": int(course["views"]),
            "preview_clicks": int(course["preview_clicks"]),
            "enrollments": int(course["enrollments"]),
            "rating": float(course["rating"]),
            "reviews": int(course["reviews"])
        })

    return results


@app.get("/api/courses/{course_id}")
def get_course_analysis(course_id: int):

    course_rows = courses[
        courses["course_id"] == course_id
    ]

    if course_rows.empty:
        return {
            "error": "Course not found"
        }

    course = course_rows.iloc[0]

    # Funnel
    funnel_data = funnel.calculate_funnel(course)

    # Retention
    retention_data = retention.calculate_retention(
        preview_events,
        course_id
    )

    # Content analysis
    content_data = content_match.analyze_content_match(
        searches,
        course_topics,
        course_id
    )

    # Diagnosis
    diagnosis_result = diagnosis.generate_diagnosis(
        funnel_data,
        retention_data,
        content_data
    )

    # Course features
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

    # ML result
    ml_row = ml_results[
        ml_results["course_id"] == course_id
    ].iloc[0]

    # Retention data for frontend chart
    retention_chart_data = []

    for _, row in retention_data.iterrows():

        retention_chart_data.append({
            "video_second": float(row["video_second"]),
            "viewers": int(row["viewers"]),
            "retention": float(row["retention"])
        })

    # Content gaps
    content_gaps = []

    for _, row in diagnosis_result["content_gaps"].iterrows():

        content_gaps.append({
            "topic": row["search_term"],
            "search_count": int(row["search_count"])
        })

    return {
        "course": {
            "course_id": int(course["course_id"]),
            "title": course["title"],
            "instructor": course["instructor"],
            "price": float(course["price"]),
            "rating": float(course["rating"]),
            "reviews": int(course["reviews"])
        },

        "funnel": {
            "views": int(funnel_data["course_views"]),
            "preview_clicks": int(funnel_data["preview_clicks"]),
            "enrollments": int(funnel_data["enrollments"]),
            "conversion_rate": float(
                funnel_data["conversion_rate"]
            )
        },

        "course_features": {
            "preview_completion_rate": float(
                preview_completion
            ),
            "average_watch_time_seconds": float(
                average_watch_time
            ),
            "content_match_score": float(
                content_match_score
            )
        },

        "retention": retention_chart_data,

        "content_gaps": content_gaps,

        "health": {
            "conversion_status": diagnosis_result[
                "conversion_status"
            ],
            "retention_status": diagnosis_result[
                "retention_status"
            ]
        },

        "ml": {
            "low_conversion": int(
                ml_row["low_conversion"]
            ),
            "prediction": int(
                ml_row["prediction"]
            )
        },

        "diagnosis": diagnosis_result["diagnosis"]
    }