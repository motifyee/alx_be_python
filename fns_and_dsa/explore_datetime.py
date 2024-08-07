from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
    print(current_date)


def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date:"))
    future_date = datetime.today() + timedelta(days=days)
    future_date = future_date.strftime("YYYY-MM-DD")
    return future_date
