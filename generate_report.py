from lib.report_generator import generate_csv_report


def main():
    """Run the report generation entry point."""
    filename = generate_csv_report()
    print(f"Report saved as {filename}")


if __name__ == "__main__":
    main()
