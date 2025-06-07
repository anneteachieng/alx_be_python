#current date and time

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date = timedelta(days=days_to_add)
    future_date = current_date + calculate_future_date

    print(future_date)
