#current date and time

import datetime

current_date = datetime.date.today()
days_to_add = int(input("Enter the number of days to add to the current date: "))
calculate_future_date = datetime.timedelta(days=days_to_add)
future_date = current_date + calculate_future_date

print(future_date)
