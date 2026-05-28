from tkinter import *

from internet_tracker import InternetTracker
from screen_tracker import ScreenTracker
from analytics import generate_chart
from analytics import export_report
from utils import calculate_score
from app_tracker import get_active_app
from database import save_data

print("GUI Started")

tracker = InternetTracker()

screen_tracker = ScreenTracker()

window = Tk()

window.title("Digital Productivity Analytics")

window.geometry("700x500")

window.configure(bg="#1e1e1e")


# =========================
# TITLE
# =========================

title = Label(
    window,
    text="Digital Productivity & Internet Analytics",
    fg="white",
    bg="#1e1e1e",
    font=("Arial", 18, "bold")
)

title.pack(pady=20)


# =========================
# INTERNET LABELS
# =========================

upload_label = Label(
    window,
    text="",
    fg="lightgreen",
    bg="#1e1e1e",
    font=("Arial", 12)
)

upload_label.pack(pady=5)


download_label = Label(
    window,
    text="",
    fg="lightblue",
    bg="#1e1e1e",
    font=("Arial", 12)
)

download_label.pack(pady=5)


# =========================
# SCREEN TIME LABEL
# =========================

screen_label = Label(
    window,
    text="",
    fg="orange",
    bg="#1e1e1e",
    font=("Arial", 12)
)

screen_label.pack(pady=5)


# =========================
# ACTIVE APP LABEL
# =========================

app_label = Label(
    window,
    text="",
    fg="yellow",
    bg="#1e1e1e",
    font=("Arial", 12)
)

app_label.pack(pady=5)


# =========================
# PRODUCTIVITY SCORE LABEL
# =========================

score_label = Label(
    window,
    text="",
    fg="pink",
    bg="#1e1e1e",
    font=("Arial", 12)
)

score_label.pack(pady=5)


# =========================
# UPDATE FUNCTION
# =========================

def update_data():

    data = tracker.get_usage()

    upload_label.config(
        text=f"Upload Speed: {data['upload_speed']} KB/s"
    )

    download_label.config(
        text=f"Download Speed: {data['download_speed']} KB/s"
    )

    hours, minutes, seconds = screen_tracker.get_screen_time()

    screen_label.config(
        text=f"Screen Time: {hours}h {minutes}m {seconds}s"
    )

    app_label.config(
        text=f"Current App: {get_active_app()}"
    )

    score = calculate_score(
        hours,
        data["total_download_mb"]
    )

    score_label.config(
        text=f"Productivity Score: {score}/100"
    )


    # SAVE DATA INTO DATABASE

    save_data(

        data["upload_speed"],
        data["download_speed"],
        data["total_upload_mb"],
        data["total_download_mb"]

    )

    window.after(1000, update_data)


# =========================
# REPORT FUNCTION
# =========================

def show_report():

    data = tracker.get_usage()

    generate_chart(
        data["total_upload_mb"],
        data["total_download_mb"]
    )


# =========================
# EXPORT REPORT FUNCTION
# =========================

def export_daily_report():

    data = tracker.get_usage()

    hours, minutes, seconds = screen_tracker.get_screen_time()

    score = calculate_score(
        hours,
        data["total_download_mb"]
    )

    export_report(
        data["total_upload_mb"],
        data["total_download_mb"],
        score
    )


# =========================
# BUTTONS
# =========================

report_button = Button(
    window,
    text="Generate Report",
    command=show_report,
    bg="green",
    fg="white",
    font=("Arial", 12)
)

report_button.pack(pady=10)


export_button = Button(
    window,
    text="Export Report",
    command=export_daily_report,
    bg="blue",
    fg="white",
    font=("Arial", 12)
)

export_button.pack(pady=10)


exit_button = Button(
    window,
    text="Exit",
    command=window.destroy,
    bg="red",
    fg="white",
    font=("Arial", 12)
)

exit_button.pack(pady=10)


# =========================
# START APPLICATION
# =========================

update_data()

window.mainloop()