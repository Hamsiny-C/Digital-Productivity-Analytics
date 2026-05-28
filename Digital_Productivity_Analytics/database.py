import sqlite3

connection = sqlite3.connect("productivity.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS internet_usage (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    upload_speed REAL,

    download_speed REAL,

    total_upload REAL,

    total_download REAL

)
""")

connection.commit()


def save_data(upload_speed, download_speed, total_upload, total_download):

    cursor.execute("""

    INSERT INTO internet_usage (

        upload_speed,
        download_speed,
        total_upload,
        total_download

    )

    VALUES (?, ?, ?, ?)

    """, (

        upload_speed,
        download_speed,
        total_upload,
        total_download

    ))

    connection.commit()