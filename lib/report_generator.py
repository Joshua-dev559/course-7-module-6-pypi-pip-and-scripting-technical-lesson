import csv
from datetime import datetime


def generate_csv_report():
    """Generate a CSV report and write mock content."""
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Status"])
        writer.writerow([1, "Complete"])

    return filename


if __name__ == "__main__":
    filename = generate_csv_report()
    print(f"Report saved as {filename}")
