import matplotlib.pyplot as plt


def create_retention_chart(retention_data, course_title):

    video_seconds = retention_data["video_second"]
    retention = retention_data["retention"]

    plt.figure(figsize=(10, 5))

    plt.plot(
        video_seconds,
        retention,
        marker="o"
    )

    plt.title(f"Preview Video Retention - {course_title}")
    plt.xlabel("Video Time (seconds)")
    plt.ylabel("Retention (%)")

    plt.ylim(0, 100)
    plt.grid(True)

    plt.tight_layout()

    plt.show()