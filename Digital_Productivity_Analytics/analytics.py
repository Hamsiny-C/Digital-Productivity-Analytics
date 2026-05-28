import matplotlib.pyplot as plt


# =========================
# GENERATE CHART FUNCTION
# =========================

def generate_chart(upload, download):

    labels = ["Upload", "Download"]

    values = [upload, download]

    plt.figure(figsize=(10, 5))


    # BAR CHART

    plt.subplot(1, 2, 1)

    plt.bar(labels, values)

    plt.title("Internet Usage")

    plt.ylabel("Usage in MB")


    # PIE CHART

    plt.subplot(1, 2, 2)

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Usage Distribution")

    plt.show()


# =========================
# EXPORT REPORT FUNCTION
# =========================

def export_report(upload, download, score):

    with open("daily_report.txt", "w") as file:

        file.write("DIGITAL PRODUCTIVITY REPORT\n")

        file.write("===========================\n\n")

        file.write(f"Upload Usage: {upload} MB\n")

        file.write(f"Download Usage: {download} MB\n")

        file.write(f"Productivity Score: {score}/100\n")

    print("Report Exported Successfully")