from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_courses():

    file_path = DATA_DIR / "courses.csv"

    try:
        data = pd.read_csv(file_path)

        print(f"Successfully loaded: {file_path}")
        print(f"Rows: {data.shape[0]}")
        print(f"Columns: {data.shape[1]}")

        return data

    except FileNotFoundError:
        print("courses.csv not found")
        return None

    except Exception as error:
        print(f"Error loading file: {error}")
        return None


def load_preview_events():

    file_path = DATA_DIR / "preview_events.csv"

    try:
        data = pd.read_csv(file_path)

        print(f"\nSuccessfully loaded: {file_path}")
        print(f"Rows: {data.shape[0]}")
        print(f"Columns: {data.shape[1]}")

        return data

    except FileNotFoundError:
        print("preview_events.csv not found")
        return None

    except Exception as error:
        print(f"Error loading preview data: {error}")
        return None