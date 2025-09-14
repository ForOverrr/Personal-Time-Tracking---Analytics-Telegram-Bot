import sqlite3
import datetime
import pandas as pd

def init_db():
    conn = sqlite3.connect("timetracker.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            activity_name TEXT NOT NULL,
            start_time DATETIME NOT NULL,
            end_time DATETIME,
            duration_minutes INTEGER
        )
    """)
    conn.commit()
    conn.close()

def start_activity(user_id: int, activity_name: str):
    conn = sqlite3.connect("timetracker.db")
    cursor = conn.cursor()
    start_time = datetime.datetime.now()

    cursor.execute(
        "INSERT INTO activities (user_id, activity_name, start_time) VALUES (?, ?, ?)",
        (user_id, activity_name, start_time)
    )
    conn.commit()
    activity_id = cursor.lastrowid
    conn.close()
    return activity_id

def stop_activity(activity_id: int):
    conn = sqlite3.connect("timetracker.db")
    cursor = conn.cursor()
    end_time = datetime.datetime.now()

    cursor.execute("SELECT start_time FROM activities WHERE id = ?", (activity_id,))
    start_time_str = cursor.fetchone()[0]
    

    start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S.%f')

    duration = end_time - start_time
    duration_minutes = int(duration.total_seconds() / 60)

    cursor.execute(
        "UPDATE activities SET end_time = ?, duration_minutes = ? WHERE id = ?",
        (end_time, duration_minutes, activity_id)
    )
    conn.commit()
    conn.close()
    return duration_minutes




def get_activities(user_id: int, period: str) -> pd.DataFrame:
    """Fetches completed activities for a given period and returns a Pandas DataFrame."""
    conn = sqlite3.connect("timetracker.db")
    today = datetime.date.today()

    if period == 'today':
        # Get all entries from the beginning of today
        start_date = datetime.datetime.combine(today, datetime.time.min)
    elif period == 'week':
        # Get all entries from the beginning of the week (Monday)
        start_of_week = today - datetime.timedelta(days=today.weekday())
        start_date = datetime.datetime.combine(start_of_week, datetime.time.min)
    else:
        # Return an empty DataFrame if the period is invalid
        return pd.DataFrame()

    query = """
        SELECT activity_name, duration_minutes
        FROM activities
        WHERE user_id = ? AND end_time IS NOT NULL AND start_time >= ?
    """
    
    df = pd.read_sql_query(query, conn, params=(user_id, start_date))
    conn.close()
    return df